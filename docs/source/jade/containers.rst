.. _containers:

Using Containerised Applications
================================


Apptainer Containers
----------------------

Apptainer 1.3.5 is installed on compute nodes, it is not available on login nodes. You should build your container, within your own environment

There are a number of converted AMD Infinity Hub Docker containers on the system, these are located in ``/apps/common/containers/apptainer/AMD``

To run an Apptainer contained application on a compute node interactively::

    srun -p short --gres=gpu:4 --pty apptainer run --rocm /apps/common/containers/apptainer/AMD/PyTorch/2.3.0/PyTorch-2.3.0-AMD.sif python PTsanitycheck.py 

The output should be as follows::

srun: GPU gres requested, checking settings/requirements...

    ############################## 

    >>>> torch.__version__
    2.3.0a0+gitd2f9472
 
    >>>> torch.cuda.is_available()
    True 

    >>>> torch.cuda.device_count()
    4 

    >>>> torch.cuda.current_device()
    0 

    >>>> torch.cuda.device(0)
    <torch.cuda.device object at 0x14db2246ff40> 

    >>>> torch.cuda.get_device_name(0)
    AMD Instinct MI300X 

    >>>> torch.cuda.device(0)
    <torch.cuda.device object at 0x14db2246ff40> 

    >>>> torch.cuda.get_device_name(0)
    AMD Instinct MI300X 

    >>>> torch.cuda.device(1)
    <torch.cuda.device object at 0x14db2246ff40> 

    >>>> torch.cuda.get_device_name(1)
    AMD Instinct MI300X 

    >>>> torch.cuda.device(2)
    <torch.cuda.device object at 0x14db2246ff40> 

    >>>> torch.cuda.get_device_name(2)
    AMD Instinct MI300X 

    >>>> torch.cuda.device(3)
    <torch.cuda.device object at 0x14db2246ff40> 

    >>>> torch.cuda.get_device_name(3)
    AMD Instinct MI300X 

    >>>> torch.zeros(2, 3)
    tensor([[0., 0., 0.],
            [0., 0., 0.]]) 

     >>>> torch.zeros(2, 3).cuda()
    tensor([[0., 0., 0.],
            [0., 0., 0.]], device='cuda:0') 

    >>>> torch.tensor([[1, 2, 3], [4, 5, 6]])
    tensor([[1, 2, 3],
            [4, 5, 6]], device='cuda:0') 

    >>>> tensor_a + cuda_zero
    tensor([[1., 2., 3.],
            [4., 5., 6.]], device='cuda:0') 

    >>>> tensor_a * cuda_twos
   tensor([[ 2.,  4.,  6.],
           [ 8., 10., 12.]], device='cuda:0') 

   >>>> torch.matmul(tensor_a, cuda_twos.T)
   tensor([[12., 12.],
           [30., 30.]], device='cuda:0') 



