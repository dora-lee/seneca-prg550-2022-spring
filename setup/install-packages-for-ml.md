

## Rebuild Python with ssl to resolve `"ssl module in Python is not available" when installing package with pip3` error. [^1]

```
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libatlas-base-dev
```
```
cd ~/software/src/Python3.9.9
sh configure --prefix=/home/pi/software
make && make install
```

## Install packages for machine learning environment [^2]

1. Install python packages
    ```
    sudo apt-get install python3-matplotlib
    sudo apt-get install python3-scipy
    sudo apt-get install python3-numpy    
    pip3 install pandas pandas-datareader scikit-learn seaborn yfinance yahoofinancials
    pip3 install bs4 requests
    ```

## Install and Connect to Jupyter Server on the Rasberry Pi [^2]

1. Install jupyter notebook environment
    ```
    pip3 install jupyter
    ```

1. Setup ssh port forwarding from Raspberry Pi to PC.
    ```
    ssh -L 8888:localhost:8888 pi@rpi-doralee.local
    ```

1. Start Jupyter server on Raspberry Pi in `/home/pi/workspace` directory
    ```
    cd workspace # you should have already created this directory in /home/pi
    jupyter notebook --no-browser
    ```

1. Once the Jupyter server starts, you'll see messages similar to below
    ```
    [I 12:18:36.226 NotebookApp] Serving notebooks from local directory: /home/pi/workspace
    [I 12:18:36.226 NotebookApp] Jupyter Notebook 6.4.11 is running at:
    [I 12:18:36.226 NotebookApp] http://localhost:8888/?token=7fcf706d39383de787d04a234caed47dc2c81e768c4a95d0
    [I 12:18:36.226 NotebookApp]  or http://127.0.0.1:8888/?token=7fcf706d39383de787d04a234caed47dc2c81e768c4a95d0
    [I 12:18:36.227 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 12:18:36.236 NotebookApp]

        To access the notebook, open this file in a browser:
            file:///home/pi/.local/share/jupyter/runtime/nbserver-8138-open.html
        Or copy and paste one of these URLs:
            http://localhost:8888/?token=7fcf706d39383de787d04a234caed47dc2c81e768c4a95d0
        or http://127.0.0.1:8888/?token=7fcf706d39383de787d04a234caed47dc2c81e768c4a95d0

    ```

1. From your PC's web browser connect to the indicated url.  From the above example, connect with this url:
    ```
    http://localhost:8888/?token=9b571a812c2bbca3d7f3a8d46d2a0b3085d4379cc12031db
    ```
    Note: the `ssh -L ... ` port forwarding session above must be active in order to connect the the Raspberry Pi's Jupyter server



[^1]: adapted from [Stack Overflow](https://stackoverflow.com/a/44758621)

[^2]: adpapted from [Setup machine learning environment in Raspberry Pi by tisutisu](https://medium.com/@tisutisu/setup-machine-learning-environment-in-raspberry-pi-bc386c6a6f40)