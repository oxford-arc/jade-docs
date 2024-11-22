.. _gromacs:

GROMACS
=======

.. sidebar:: GROMACS

  :URL: http://www.gromacs.org/
  :URL: https://www.nvidia.com/en-us/data-center/gpu-accelerated-applications/gromacs/


GROMACS is a versatile package for molecular dynamics simulations, which solves the Newtonian equations of motion for systems with hundreds to millions of particles.  Although the software scales well to hundreds of cores for typical simulations, GROMACS calculations are restricted to at most a single node on the JADE service.

Job scripts
-----------

GROMACS jobs can run using 1, 4 (half a node), or 8 (full node) GPUs (please see note below regarding job performance). The following SLURM script example is written for one of the regression tests from the installation:


::

   #!/bin/bash

   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=1
   #SBATCH --cpus-per-task=5
   #SBATCH --gres=gpu:1
   #SBATCH --gres-flags=enforce-binding
   #SBATCH --time=10:00:00
   #SBATCH -J testGromacs
   #SBATCH -p small

   module purge
   module use /apps/system/modules
   module use /apps/system/easybuild/modules/all

   module load GROMACS/2024.3-foss-2024a-mpi

   mpirun -np ${SLURM_NTASKS_PER_NODE} --bind-to socket \
          mdrun_mpi -s topol.tpr \
	  -ntomp ${SLURM_CPUS_PER_TASK} &> run-gromacs.out


The example utilises 1 GPU (--gres=gpu:1) on a JADE node. GROMACS is started with a number of MPI processes (--ntasks-per-node=1) , which must match the number of requested GPUs. Each MPI process will run 5 OMP threads (--cpus-per-task=5). The number of requested MPI processes is saved in the environment variable SLURM_NTASKS_PER_NODE, while the number of threads per process is saved in SLURM_CPUS_PER_TASK.

The request --bind-to socket is specific to OpenMPI, which was used to build GROMACS on JADE. This extra option to the OpenMPI mpirun is essential in obtaining the optimal run configuration and computational performance.


