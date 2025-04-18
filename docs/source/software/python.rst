.. _python-conda:

Python
======

.. sidebar:: Python

   :URL: https://python.org
   :URL: https://www.anaconda.com


This page documents the python and Anaconda installation on JADE. This is the
recommended way of using Python, and the best way to be able to configure custom
sets of packages for your use.

"conda" a Python package manager, allows you to create "environments" which are
sets of packages that you can modify. It does this by installing them in your
home area. This page will guide you through loading conda and then creating and
modifying environments so you can install and use whatever Python packages you
need.

Using standard Python
---------------------

Standard Python 3 is available to be loaded as a module: ::

  Python/3.12.3-GCCcore-13.3.0
  

Use the ``module load`` command to load a particular version of python 
e.g. for Python 3.12.3: ::

  module load Python/3.12.3-GCCcore-13.3.0

Using conda Python
------------------

Miniconda/Anaconda versions are available for Python 3 and can be loaded through provided module files: ::

  Anaconda3/2024.02-1
  Miniconda3/23.10.0-1

Use the ``module load`` command to load a particular Conda Python version e.g. Miniconda for Python 3: ::

  module load Miniconda3/23.10.0-1


Using conda Environments
########################

Once the conda module is loaded you have to load or create the desired
conda environments. For the documentation on conda environments see
`the conda documentation <http://conda.pydata.org/docs/using/envs.html>`_.

You can load a conda environment with::

    source activate python3

where ``python3`` is the name of the environment, and unload one with::

    source deactivate

which will return you to the ``root`` environment.

It is possible to list all the available environments with::

    conda env list


Creating an Environment
#######################

Every user can create their own environments, and packages shared with the
system-wide environments will not be reinstalled or copied to your file store.

To create a clean environment with just Python 3 and numpy you can run::

    conda create -n mynumpy python=3.10 numpy

This will download the latest release of Python 3.10 and numpy, and create an
environment named ``mynumpy``.

Any version of Python or list of packages can be provided::

    conda create -n myscience python=3.9 numpy=1.8.1 scipy

If you wish to modify an existing environment, such as one of the anaconda
installations, you can ``clone`` that environment::

    conda create --clone anaconda3-4.2.0 -n myexperiment

This will create an environment called ``myexperiment`` which has all the
anaconda 4.2.0 packages installed with Python 3.


Installing Packages Inside an Environment
#########################################

Once you have created your own environment you can install additional packages
or different versions of packages into it. There are two methods for doing
this, ``conda`` and ``pip``, if a package is available through conda it is
strongly recommended that you use conda to install packages. You can search for
packages using conda::

    conda search pandas

then install the package using::

    conda install pandas

if you are not in your environment you will get a permission denied error
when trying to install packages, if this happens, create or activate an
environment you own.

If a package is not available through conda you can search for and install it
using pip, *i.e.*::

    pip search colormath

    pip install colormath
