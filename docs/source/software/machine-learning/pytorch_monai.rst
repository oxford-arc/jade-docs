.. _pytorch:

PyTorch and MONAI
=================

This is a simple guide to using PyTorch via the provided Apptainer container on JADE. This will cover basic script 
setup with SLURM and invoking a PyTorch script. A more involved example is given using the MONAI biomedical deep
learning framework.

The following instructions will use the container ``/apps/common/containers/apptainer/AMD/PyTorch/2.3.0/PyTorch-2.3.0-AMD.sif``
and demonstrate data and scratch directories. The version of PyTorch in this container is specific to the AMD hardware on
JADE and so shouldn't be updated, however other libraries can be installed at runtime to customise the environment.

This expects that you're familiar with:
  * How to log into JADE
  * SLURM and batch scripts
  * Python and PyTorch deep learning
  * bash usage

PyTorch
-------

As demonstrated elsewhere, PyTorch can be invoked in an interactive job using the container and a Python script. First,
write the following into your home directory as the file ``pytorch_check.py``: 

.. code-block:: python

    import torch

    print("Version:", torch.__version__)
    print("Devices:", torch.cuda.device_count())

    for i in range(torch.cuda.device_count()):
        print("Device", i, ":", torch.cuda.get_device_properties(i))
      
This can then be run through an interactive job: 

.. code-block:: bash

    $ CONTAINER=/apps/common/containers/apptainer/AMD/PyTorch/2.3.0/PyTorch-2.3.0-AMD.sif
    $ srun -p short --gres=gpu:2 --pty apptainer run --rocm $CONTAINER python pytorch_check.py
    srun: GPU gres requested, checking settings/requirements...
    Version: 2.3.0a0+gitd2f9472
    Devices: 2
    Device 0 : _CudaDeviceProperties(name='AMD Instinct MI300X', major=9, minor=4, gcnArchName='gfx942:sramecc+:xnack-', total_memory=196592MB, multi_processor_count=304)
    Device 1 : _CudaDeviceProperties(name='AMD Instinct MI300X', major=9, minor=4, gcnArchName='gfx942:sramecc+:xnack-', total_memory=196592MB, multi_processor_count=304)

Submitting batch scripts is the correct method for submitting long running jobs to JADE. The equivalent script, saved to
``pytorch_check.sh`` will perform the same operation using the same Apptainer image:

.. code-block:: bash

    #!/bin/bash

    # set partition
    #SBATCH --partition=short

    # set the number of nodes
    #SBATCH --nodes=1

    # set number of CPUs
    #SBATCH --cpus-per-task=8

    # set max wallclock time
    #SBATCH --time=00:05:00

    # set name of job
    #SBATCH --job-name=pytorchtest

    # set number of GPUs
    #SBATCH --gres=gpu:2

    # container to run commands in
    CONTAINER=/apps/common/containers/apptainer/AMD/PyTorch/2.3.0/PyTorch-2.3.0-AMD.sif

    # runs the script pytorch_check.py in the container
    apptainer run --rocm "$CONTAINER" python pytorch_check.py

Once submitted with ``sbatch pytorch_check.sh``, a log file will eventually appear with the same output as above. 
Apptainer by default makes the user's home directory available in the running container but other directories need
to be bound to locations in the container on the command line. These would normally include the data and scratch
directories, which will be discussed in the next section.


MONAI
-----

The Medical Open Network for Artificial Intelligence (MONAI, https://monai.io) is a PyTorch-based framework for medical 
imaging developed in collaboration with King's College London, Nvidia, and many other consortium partners. 

This tutorial will go through downloading the test dataset, using the DATA and scratch directories effectively, and 
training a simple MLP classifier. The DATA directory is pointed to by an environment variable present in your login
session but corresponds to the location ``/data/$PROJECT/$USER``. The ``/scratch`` partition is a fast file system used for
loading data efficiently but is only available within running jobs, so the script for a batch job must move data there
before it's used. These concepts will be demonstrated here with job scripts using MONAI.

To use MONAI in the PyTorch container, it first must be installed along with dependencies. This is done with ``pip`` before
anything is run, which has the effect of installing packages into your home ``~/.local/lib/python3.10/site-packages``
directory as a result of how Apptainer makes your home directory available by default (unlike Docker).
It's important to be aware that this places some installed components in a location that isn't ephemeral and so changes 
your environment.

The previous example batch script simply ran ``python`` within the container with the script file in your home directory.
To install MONAI and then use it we would need to run a bash script within the container which does this, but instead
the "here document" feature of bash can be used in the submission script to run these commands. In the following, any
commands between ``_EOF_`` will be run within the container and so saves having to create another file:

.. code-block:: bash

    #!/bin/bash

    #SBATCH --partition=short
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=8
    #SBATCH --time=00:05:00
    #SBATCH --job-name=monaitest
    #SBATCH --gres=gpu:1

    CONTAINER=/apps/common/containers/apptainer/AMD/PyTorch/2.3.0/PyTorch-2.3.0-AMD.sif

    # runs commands in the container until _EOF_ is reached, put your actual script commands here
    apptainer run --rocm "$CONTAINER" << _EOF_
      # installs locally into ~/.local since the running container is read-only
      pip install monai[ignite,nibabel,scipy]==1.4.0
      # run your script here instead of this example
      python -m monai.config.deviceconfig
    _EOF_

Submitting this should produce a output log with MONAI's configuration information. The key thing being done here is
installing MONAI with a selection of dependencies with ``monai[ignite,nibabel,scipy]``, but avoiding installing new 
versions of PyTorch or replacing anything depending on it. This PyTorch is specifically compiled for the system's
hardward so shouldn't be replaced, but other things compatible with PyTorch 2.3.0 can be installed. 

The version of MONAI is also pinned here at 1.4.0 since later versions will drop support for PyTorch 2.3.0. Later
versions of MONAI can be installed with this unsupported version, however ensure ``pip`` doesn't replace the 
pre-compiled version in the container by including ``torch==2.3.0a0+gitd2f9472`` with the command.

Training Script
---------------

Next, download the MedNIST dataset to your data directory with the following:

.. code-block:: bash

    wget https://github.com/Project-MONAI/MONAI-extra-test-data/releases/download/0.8.1/MedNIST.tar.gz -O $DATA/MedNIST.tar.gz

This will place the file in your ``$DATA`` directory provided to you by the JADE environment. Your home directory quota 
is very small so this storage space is necessary for large datasets. The file system is however not very fast so the 
tarball will be left compressed for now and will instead be unpacked in the  running job into the scratch location.

The script below is derived from https://github.com/Project-MONAI/tutorials/blob/main/2d_classification/monai_101.ipynb
so refer to that tutorial on what exactly is being done here. This should be saved to the file ``monai_101.py``:

.. code-block:: python

    import logging
    import numpy as np
    import os
    from pathlib import Path
    import sys
    import tempfile
    import torch

    from monai.apps import MedNISTDataset
    from monai.config import print_config
    from monai.data import DataLoader
    from monai.engines import SupervisedTrainer
    from monai.handlers import StatsHandler
    from monai.inferers import SimpleInferer
    from monai.networks import eval_mode
    from monai.networks.nets import densenet121
    from monai.transforms import LoadImageD, EnsureChannelFirstD, ScaleIntensityD, Compose

    print_config()

    directory = os.environ.get("MONAI_DATA_DIRECTORY")
    if directory is not None:
        os.makedirs(directory, exist_ok=True)
    root_dir = tempfile.mkdtemp() if directory is None else directory
    print(root_dir)

    transform = Compose(
        [
            LoadImageD(keys="image", image_only=True),
            EnsureChannelFirstD(keys="image"),
            ScaleIntensityD(keys="image"),
        ]
    )

    dataset = MedNISTDataset(
        root_dir=root_dir, transform=transform, section="training", download=True, progress=False
    )

    max_epochs = 5
    model = densenet121(spatial_dims=2, in_channels=1, out_channels=6).to("cuda:0")

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    trainer = SupervisedTrainer(
        device=torch.device("cuda:0"),
        max_epochs=max_epochs,
        train_data_loader=DataLoader(dataset, batch_size=512, shuffle=True, num_workers=4),
        network=model,
        optimizer=torch.optim.Adam(model.parameters(), lr=1e-5),
        loss_function=torch.nn.CrossEntropyLoss(),
        inferer=SimpleInferer(),
        train_handlers=StatsHandler(),
    )

    trainer.run()

    dataset_dir = Path(root_dir, "MedNIST")
    class_names = sorted(f"{x.name}" for x in dataset_dir.iterdir() if x.is_dir())
    testdata = MedNISTDataset(
        root_dir=root_dir, transform=transform, section="test", download=False, progress=False
    )

    max_items_to_print = 10
    with eval_mode(model):
        for item in DataLoader(testdata, batch_size=1, num_workers=0):
            prob = np.array(model(item["image"].to("cuda:0")).detach().to("cpu"))[0]
            pred = class_names[prob.argmax()]
            gt = item["class_name"][0]
            print(f"Class prediction is {pred}. Ground-truth: {gt}")
            max_items_to_print -= 1
            if max_items_to_print == 0:
                break

We can now create ``monai_101.sh`` and submit it:

.. code-block:: bash

    #!/bin/bash

    #SBATCH --partition=short
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=8
    #SBATCH --time=01:00:00
    #SBATCH --job-name=monaitest
    #SBATCH --gres=gpu:1

    # don't exit on error to ensure cleanup is done
    set +e

    CONTAINER=/apps/common/containers/apptainer/AMD/PyTorch/2.3.0/PyTorch-2.3.0-AMD.sif
    # location of a scratch directory to use for temporary data
    SCRATCH=/scratch/slurm-$SLURM_JOBID
    # make a scratch temporary location
    mkdir -p "$SCRATCH"

    apptainer run --rocm --bind "$DATA:/data" --bind "$SCRATCH:/scratch" "$CONTAINER" << _EOF_
      pip install monai[ignite,tqdm,pillow]==1.4.0

      # copy pre-downloaded data to the fast scratch location bound in the container to /scratch
      cp /data/MedNIST.tar.gz /scratch
      # set location used in monai_101.py for finding data
      export MONAI_DATA_DIRECTORY=/scratch

      python monai_101.py
    _EOF_

    # delete temporary data
    rm -rf $SCRATCH


This job will install MONAI if not present along with dependencies and then run the Python script within the container.
The above script can be used as a template for other PyTorch training jobs by changing the contents between ``_EOF_`` 
to run other things in the container with access to both the data and scratch locations. For MONAI or other Python training
runs, replacing ``monai_101.py`` as the executed script file may be sufficient for simple set ups. 

Note that your ``$DATA`` directory is mounted (or bound) within the running container at ``/data``, this is done with the
``--bind "$DATA:/data"`` argument in the ``apptainer`` command line. Similarly, the scratch directory that was created 
for the job is bound to ``/scratch``. The typical practice is to load data from ``/data`` when needed but to rely on the
scratch location for fast disk access for intermediate results or caching. Here the tarball is copied from ``/data``
into ``/scratch`` with the expectation that the script will unpack it there and load files much faster this way. As your
code and workflow will differ from what's illustrated here, it's up to you to determine how to handle data and where
to place it for performance. 