.. _getting-started:

Using the JADE\@ARC Facility
===========================


**Accounts**

Users get accounts on the system by following the directions in the **Getting an account** section, on the left.

New users must provide a public SSH key and are given a user ID on JADE.  Using this ID, they will then be able to login to one of the head nodes by using an SSH command.

Further details are in the section **Connecting to the cluster using SSH**.


**Software**

The software packages already installed on the system comes in two kinds: *standard applications* and *containerised applications* (various Machine Learning applications in particular).  These are described further in the **Software on JADE** section on the left.

The *module* system is used to control your working environment and the particular version of software which you want to use; details are given in the section **The `module` tool** on the left.

If not using the installed software, you are also welcome to build your own applications.  Codes should be built using an interactive session on a compute node (not on the login nodes), and a number of compilers and MPI library stacks are available via the modules.


**Running applications**

Applications can only be run on the compute nodes by submitting jobs to the SLURM batch queuing system.  Examples of Slurm submission scripts are given in the relevant sections for each of the main software packages.

It is also possible to obtain an interactive session through SLURM on one of the compute nodes.  This is usually only for code development
purposes; submitting batch jobs is the standard way of working.


**Storage**

The global file system is accessible from both the head nodes and the compute nodes.  Any files written during the job execution on the compute nodes will be found on the file system after the job has completed.


There is also access to scratch disc space, but this access only possible during a SLURM job and once the job is completed the local disc data is removed automatically.  In machine learning applications, for example, this scratch space (provided by fast SSD) may be useful as a staging point for very large training sets.



.. toctree::
   :maxdepth: 2
   :glob:

   getting-account
   connecting
   modules
   scheduler/index
   containers
