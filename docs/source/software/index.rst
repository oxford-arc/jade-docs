.. _software:

Software on JADE
================

The software initially installed on the machine is listed in the following table:

.. csv-table::
   :header: Application,Version,Note
   :widths: 20, 20, 10

    GNU compiler suite,	13.3.0,	
    GNU compiler suite,	12.3.0,
    OpenMPI,   5.0.3, Inlcudes multi-thread support
    Gromacs,	2024.3,	
    

This software has been built from source and installed as modules. To list the source built applications do:

::

   $ module avail
   ---------------------------------------------------------------------------------------------------------- /apps/system/modules -----------------------------------------------------------------------------------------------------------
   AMD-LLVM/6.2.1-foss-2024a        AdaptiveCpp/24.06.0-foss-2024a-ROCm-6.2.1    AdaptiveCpp/24.06.0-foss-2024a (D)    GROMACS/2024.3-foss-2024a-tmpi (D)
   AMD-LLVM/6.2.2-foss-2024a (D)    AdaptiveCpp/24.06.0-foss-2024a-ROCm-6.2.2    GROMACS/2024.3-foss-2024a-mpi
   ---------------------------------------------------------------------------------------------------- /apps/system/easybuild/modules/all ----------------------------------------------------------------------------------------------------
   Anaconda3/2024.02-1                      FlexiBLAS/3.4.4-GCC-13.3.0         OpenSSL/1.1.1w-GCCcore-12.3.0         XZ/5.4.5-GCCcore-13.3.0             help2man/1.49.3-GCCcore-12.3.0            make/4.4.1-GCCcore-12.3.0
   Autoconf/2.71-GCCcore-12.3.0             GCC/12.3.0                         OpenSSL/3                      (D)    Z3/4.13.0-GCCcore-13.3.0            help2man/1.49.3-GCCcore-13.3.0     (D)    make/4.4.1-GCCcore-13.3.0         (D)
   Autoconf/2.72-GCCcore-13.3.0      (D)    GCC/13.3.0                  (D)    PMIx/5.0.2-GCCcore-13.3.0             binutils/2.40-GCCcore-12.3.0        hwloc/2.10.0-GCCcore-13.3.0               ncurses/6.4-GCCcore-12.3.0
   Automake/1.16.5-GCCcore-12.3.0           GCCcore/12.3.0                     PRRTE/3.0.5-GCCcore-13.3.0            binutils/2.40                       libarchive/3.7.4-GCCcore-13.3.0           ncurses/6.5-GCCcore-13.3.0
   Automake/1.16.5-GCCcore-13.3.0    (D)    GCCcore/13.3.0              (D)    Perl/5.36.1-GCCcore-12.3.0            binutils/2.42-GCCcore-13.3.0        libevent/2.1.12-GCCcore-12.3.0            ncurses/6.5                       (D)
   Autotools/20220317-GCCcore-12.3.0        GMP/6.3.0-GCCcore-13.3.0           Perl/5.38.0                           binutils/2.42                (D)    libevent/2.1.12-GCCcore-13.3.0     (D)    numactl/2.0.16-GCCcore-12.3.0
   Autotools/20231222-GCCcore-13.3.0 (D)    ICU/75.1-GCCcore-13.3.0            Perl/5.38.2-GCCcore-13.3.0     (D)    bzip2/1.0.8-GCCcore-12.3.0          libfabric/1.18.0-GCCcore-12.3.0           numactl/2.0.18-GCCcore-13.3.0     (D)
   BLIS/1.0-GCC-13.3.0                      LAPACK/3.12.0-GCC-13.3.0           Python/3.12.3-GCCcore-13.3.0          bzip2/1.0.8-GCCcore-13.3.0   (D)    libfabric/1.21.0-GCCcore-13.3.0    (D)    pkgconf/1.8.0
   Bison/3.8.2-GCCcore-12.3.0               LLVM/18.1.8-GCCcore-13.3.0         SQLite/3.42.0-GCCcore-12.3.0          cURL/8.0.1-GCCcore-12.3.0           libffi/3.4.4-GCCcore-12.3.0               pkgconf/1.9.5-GCCcore-12.3.0
   Bison/3.8.2-GCCcore-13.3.0               M4/1.4.19-GCCcore-12.3.0           SQLite/3.45.3-GCCcore-13.3.0   (D)    cURL/8.7.1-GCCcore-13.3.0    (D)    libffi/3.4.5-GCCcore-13.3.0        (D)    pkgconf/2.2.0-GCCcore-13.3.0      (D)
   Bison/3.8.2                       (D)    M4/1.4.19-GCCcore-13.3.0           ScaLAPACK/2.2.0-gompi-2024a-fb        fio/3.36-GCCcore-12.3.0             libpciaccess/0.17-GCCcore-12.3.0          xorg-macros/1.20.0-GCCcore-12.3.0
   Boost/1.85.0-GCC-13.3.0                  M4/1.4.19                   (D)    Tcl/8.6.13-GCCcore-12.3.0             flex/2.6.4-GCCcore-12.3.0           libpciaccess/0.18.1-GCCcore-13.3.0 (D)    xorg-macros/1.20.1-GCCcore-13.3.0 (D)
   CMake/3.29.3-GCCcore-13.3.0              Meson/1.4.0-GCCcore-13.3.0         Tcl/8.6.14-GCCcore-13.3.0      (D)    flex/2.6.4-GCCcore-13.3.0           libreadline/8.2-GCCcore-12.3.0            zlib/1.2.13-GCCcore-12.3.0
   Clang/18.1.8-GCCcore-13.3.0              Miniconda3/23.10.0-1               UCC/1.3.0-GCCcore-13.3.0              flex/2.6.4                   (D)    libreadline/8.2-GCCcore-13.3.0     (D)    zlib/1.2.13
   EasyBuild/4.9.4                          Ninja/1.12.1-GCCcore-13.3.0        UCX/1.14.1-GCCcore-12.3.0             foss/2024a                          libtool/2.4.7-GCCcore-12.3.0              zlib/1.3.1-GCCcore-13.3.0
   FFTW.MPI/3.3.10-gompi-2024a              OpenBLAS/0.3.27-GCC-13.3.0         UCX/1.16.0-GCCcore-13.3.0      (D)    gettext/0.22.5                      libtool/2.4.7-GCCcore-13.3.0       (D)    zlib/1.3.1                        (D)
   FFTW/3.3.10-GCC-12.3.0                   OpenMPI/5.0.3-GCC-13.3.0           UnZip/6.0-GCCcore-12.3.0              gompi/2024a                         libxml2/2.12.7-GCCcore-13.3.0             zstd/1.5.6-GCCcore-13.3.0
   FFTW/3.3.10-GCC-13.3.0            (D)    OpenSSL/1.1                        UnZip/6.0-GCCcore-13.3.0       (D)    gzip/1.13-GCCcore-13.3.0            lz4/1.9.4-GCCcore-13.3.0

   


The following are the available applications, libraries and development tools on the JADE cluster:

.. toctree::
    :maxdepth: 2
    :glob:

    molecular-dynamics/index
    python
    git
    
