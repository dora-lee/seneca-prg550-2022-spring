<img src="../images/senecac.gif" alt="Seneca College" height="38" width="349" />

# Setting up the tools

1. [Install Python on Windows](install-python-windows.md) **-OR-** [Install Python for MacOS](install-python-macos.md)

1. [Setup Raspberry Pi OS](config-image-raspberry-pi-os.md)

1. [Install and build Python3 on the Raspberry Pi](install-python3-from-src.md)

1. Interactive debugging is available through Python’s [Integrated Development and Learning Environment](https://docs.python.org/3/library/idle.html) (IDLE) shell window
    1. run `python3` from the command-line and interactively execute python commands at the `>>>` prompt
    ```
    Python 3.9.9 (main, May 30 2022, 22:44:39)
    [GCC 10.2.1 20210110] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```    

1. (Optional) Code development on the Raspberry Pi
    1. The [Geany](https://www.geany.org/) text editor is part of the installed image.  Run `geany` from the Raspberry Pi's command line to start
    1. `cd` to the directory containing the file you have open (ex: `my_file.py`) in geany and run `python3 my_code.py` to test the code

1. (Optional) [Setup VSCode remote editing](vscode_rpi_remote_edit.md)

1. (Optional) [Setup wifi for Seneca's lab environment](config-seneca-wifi.md)