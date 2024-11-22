.. _connecting:

Connecting to the cluster using SSH
===================================

To log onto the JADE cluster you must use `SSH <https://en.wikipedia.org/wiki/Secure_Shell>`_, which is a common way of remotely logging in to computers running the GNU/Linux operating system.

To do this, you need to have a SSH *client* program installed on your machine. GNU/Linux, macOS and recent Windows versions come with a command-line (text-only) SSH client pre-installed.  For Windows there are also various graphical SSH clients you can use, including *MobaXTerm*.

.. _connecting-ssh-client-windows:

SSH client software on Windows
------------------------------

Download and install the *Installer edition* of `mobaxterm <https://mobaxterm.mobatek.net/download-home-edition.html>`_.

After starting MobaXterm you should see something like this:

.. image:: /images/mobaxterm-welcome.png
   :width: 50%
   :align: center

Click *Start local terminal* and if you see something like the following then please continue to :ref:`ssh-connection`.

.. image:: /images/mobaxterm-terminal.png
   :width: 50%
   :align: center

Running commands from a terminal (from the command-line) may initially be
unfamiliar to Windows users but this is the recommended approach for
running commands on JADE as
it is the idiomatic way of interfacing with the GNU/Linux clusters.

SSH client software on Mac OS/X and GNU/Linux
---------------------------------------------

GNU/Linux and macOS (OS X) both typically come with a command-line SSH client pre-installed.

If you are using macOS and want to be able to run graphical applications on the clusters then
you need to install the latest version of the `XQuartz <https://www.xquartz.org/>`_ *X Windows server*.

Open a terminal (e.g. *Gnome Terminal* on GNU/Linux or *Terminal* on macOS) and then go to :ref:`ssh-connection`.

.. _connecting-generate-ssh-keys:

Generating SSH Keys
-------------------

SSH keys allows you to connect remotely to JADE through SSH without the need for passwords. When generating
SSH keys, a pair of public (normally with .pub extension) and private keys are generated.

You will need to provide your SSH *public* key as part of your SAFE account registration process. *Your private key
should never be shared with anybody else* and will be used by your SSH client when connecting to JADE  (e.g. ssh on the
command line or MobaXterm).

#. Open your preferred terminal/shell/command line app (for Windows, see :ref:`connecting-ssh-client-windows`).
#. Type in: ::

    ssh-keygen -t rsa

#. You will be asked where you'd like to save the key. Just pressing enter will save to a default location at ``/home/[yourusername]/.ssh/id_rsa``).
#. You will then be asked for a passphrase of the key. It is recommended to set a strong passphrase.
#. You will have to confirm your passphrase.
#. Your key is now generated and written to the location you specified. 
   
   There should be two files, a private key without an extension (e.g. ``id_rsa``) and public key with a ``.pub`` extension (e.g. ``id_rsa.pub``)
#. When registering for a JADE account, you will need to send us your public key file (.pub extension).

An example of the output can be seen below: ::

    $ ssh-keygen -t rsa
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/my_username/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/my_username/.ssh/id_rsa
    Your public key has been saved in /home/my_username/.ssh/id_rsa.pub
    The key fingerprint is:
    SHA256:weZ3rpaY5kV0OKX8Z6hTlxpAso6ZOaARtpgUYHk18rI my_username@my_machine_name
    The key's randomart image is:
    +---[RSA 3072]----+
    |o+=..o  . . .    |
    |o= +o .. = +     |
    |o +...  = B .    |
    |   oo. O o = . . |
    |  .E  * S o * =  |
    |       . o = *   |
    |         o+.o    |
    |        +.oo     |
    |       o...      |
    +----[SHA256]-----+

.. note::
    MobaXterm has its own ``home`` directory path which can be opened using the command ``open /home/mobaxterm``. You can then place key files generated externally into the ``.ssh`` folder.

.. _ssh-connection:

Establishing a SSH connection
-----------------------------

Once you have a terminal open, run the following command to log into one of the JADE front-end nodes: ::

  ssh -l $USER jade-login.arc.ox.ac.uk

Here you need to replace ``$USER`` with your username (e.g. ``jade1234``).

.. note::
   
   If you have a key file named ``id_rsa`` in your home's ``.ssh`` directory, it will be used by default. You can manually specify a key's path by adding an ``-i`` flag if your key has a different name or is in a different location e.g.
   
   ``ssh -l $USER -i /home/my_username/.ssh/my_custom_key jade-login.arc.ox.ac.uk`` 
   
   or set up your ``/home/my_username/.ssh/config`` file to specify which key to use for which host. 

.. warning::
    When first connecting, SSH will usually present you with the hosts' public SSH key and ask to confirm it. This is to allow SSH to verify the host you are connecting to; should that key change, you will be warned by SSH as this could potentially indicate a man-in-the-middle attack. 

    The host keys for jade-login.arc.ox.ac.uk for various key algorithms are:
    .. csv-table:: jade-login.arc.ox.ac.uk SSH keys
       :file: jade_ssh_keys.csv
       :widths: 30, 70
       :header-rows: 1
    
    If the host keys presented by the system do not match these keys please do not accept the connection and get in touch with ``jade-support@arc.ox.ac.uk`` as soon as possible.


When you login to a cluster you reach one of two login nodes.
    
You **should not** run applications on the login nodes; nor should they be used for e.g. code compilation. They are not designed for this purpose; they are not running the same OS as the worker nodes; and they are of a different CPU architecture.

Running ``srun`` gives you an interactive terminal on one of the worker nodes in the cluster.
 
