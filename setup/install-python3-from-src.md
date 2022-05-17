
<span><img src="../images/senecac.gif" alt="Seneca College" height="38" width="349" /></span>

# Installing Python 3.9.9 for Raspbian on a Raspberry Pi 3B+/4

<a href="http://www.python.org" target="_blank"><img src="../images/python-logo.png" height="82" width="290" alt="www.python.org" /></a>


This page describes how to install the Python programming
interpretor (v. 3.9.9) on a Raspberry Pi (running the Raspbian Desktop OS).

You will require at least >60.1 Mb of free disk space as well as
the GCC >4.0 (C language) development tools (along with the "make" utility).
The default installation installs Python in the /usr/local/ directory,
but these instructions will specify how to install python in your own
user account in the /home/pi/software/ directory on your Raspberry Pi.

NOTE: Once the install has completed, you will have to ensure that
      you have the path to the Python interpretor listed in your $PATH
      environment variable in order to use this distribution (3.9.9).
      Therefore, please [FIRST follow this tutorial](config-image-raspberry-pi-os.md) for setting up your terminal environment
      BEFORE proceeding with this installation!
      
Start a terminal and you should be able to enter shell commands at the ```/home/pi>``` prompt.

To test which version of Python you are using, and where python is installed
on your system, you can execute the following shell commands from the Terminal

```/home/pi>```
```
which python3
```

The response should be similar to:
```
pi@raspberrypi:~ $ which python3
/usr/bin/python3
```

<span class="c9d">STEP 1:</span> Login to your Raspberry Pi (the default user id should
be ```pi```). The default password will be what you've set during the OS-imaging stage.  You can change this using
the `passwd` command. Open a Terminal window.

<span class="c9d">STEP 2:</span> Create the ```software/``` directory.
In your pi user account, create a directory called "software" by issuing the
following command:

```/home/pi>```
```
mkdir software
```
<span class="c9d">STEP 3:</span> Change directories to the ```/software``` directory.
```
cd /software
```
<span class="c9d">STEP 4a:</span> Create a new sub-directory called
```src``` by issuing the following command:

```/home/pi/software>```
```
mkdir src
```
<span class="c9d">STEP 4b:</span> Change to the ```src/``` directory:
```
cd src
```
<span class="c9d">STEP 4c:</span> Download the Python 3.9.9 source tree using `curl`:

```/home/pi/software/src>```
```
curl -O https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz
```
<span class="c9d">STEP 4d:</span> Now, before compiling the Python distribution, some additional
developent tools and libraries/packages will be required.
Issue the following commands one at a time until each is completed:

```/home/pi/software/src>```
```
sudo apt install libbz2-dev -y \
libgdbm-dev -y \
libsqlite3-dev -y \
libssl-dev -y \
libreadline6-dev -y \
liblzma-dev -y \
zlib1g-dev -y tk-dev -y \
libgdbm-dev -y \
libffi-dev -y \
libncurses5-dev -y
```
<span class="c9d">STEP 5:</span> Extract the Python installation source tree.

```/home/pi/software/src>```
```
tar -xzf Python-3.9.9.tgz
```

This will create a new directory 'Python-3.9.9' in the ```/home/pi/software/src```
directory containing the source code for the distribution.
You must ```cd``into that directory before proceeding with configuration
and compiling the source.

<span class="c9d">STEP 6:</span> Change directories.

```/home/pi/software/src>```
```
cd Python-3.9.9
```

<span class="c9d">STEP 7:</span> Configure the Python installation:
PLEASE TAKE NOTE OF THE SPECIAL INSTRUCTION HERE!

```/home/pi/software/src/Python-3.9.9>```
```
sh configure --prefix=/home/pi/software
```

<span class="c9d">STEP 8:</span> Build.
This next step will now compile all of the source files into
a machine-specific binary (python3) that can be run from the shell.
NOTE: Depending on the speed of your Raspberry Pi's CPU, this may take several minutes
to complete.

```/home/pi/software/src/Python-3.9.9>```
```
make
```

<span class="c9d">STEP 9:</span> Install.
Once compiled, your Python distribution can now be installed
on your system in your pi account (including the addition
of man pages).

```/home/pi/software/src/Python-3.9.9>```
```
make install
```


<span class="c9d">STEP 13:</span> Now move back to your home directory by entering the cd command.

```/home/pi/software/src/Python-3.9.9>```
```
cd
```

Now enter the following command:

```/home/pi>```
```
. .profile
```

You can now test your system by running the following commands:

```/home/pi>```
```
python3 -V
whereis python3
which python3
```

If you see the following message then you've properly compiled and installed Python on your Raspberry Pi!
```
/home/pi> python3 -V
Python 3.9.9

/home/pi> whereis python3
python3: /usr/bin/python3.9 /usr/bin/python3 /usr/bin/python3.9-config /usr/lib/python3.9 /usr/lib/python3 /etc/python3.9 /etc/python3 /usr/local/lib/python3.9 /usr/include/python3.9 /usr/include/python3.9m /usr/share/python3 /usr/share/man/man1/python3.1.gz

/home/pi >which python3
/home/pi/software/bin/python3
```

Congratulations, that's it!
