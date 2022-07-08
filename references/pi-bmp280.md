<span><img src="../images/senecac.gif" alt="Seneca College" height="38" width="349" /></span>
# BMP280 and the Raspberry Pi

This page provides instructions to install and configure libraries, and wiring diagram to connect the BMP280 temperature and pressure sensor to your Raspberry Pi.

<p align="center">
<img src="../labs/images/bmp280_pi_connection.png" alt="Raspbery Pi and BMP280 Wiring Diagram" width="400" />
</p>

## Connecting the BMP260 sensor to the Raspberry Pi via I2C [^1]

1. Install [Adafruit Python libraries](https://pypi.org/project/adafruit-circuitpython-bmp280/) to interface with the BMP280

    ```
    # will also install the needed `board` module as a dependency
    pip3 install --upgrade adafruit-python-shell

    # install bmp280 module
    pip3 install adafruit-circuitpython-bmp280
    ```

1. Enable I2C interface:
    1. run `sudo raspi-config`
        1. --> Interface Options --> I2C --> "Would you like the ARM I2C interface to be enabled?"
        
            Answer "Yes"
        1. Exit `raspi-config`

1. Validate I2C interface is functional from command line:

    ```
    # show active I2C ports
    i2cdetect -l 
    ```

    Your output should look similar to
    ```
    /home/pi >i2cdetect -l
    i2c-1   i2c             bcm2835 (i2c@7e804000)                  I2C adapter
    i2c-2   i2c             bcm2835 (i2c@7e805000)                  I2C adapter
    ```

1. Connect the BMP280 according to wiring diagram above and validate connection by running `i2cdetect` tool.   
    ```    
    # get address for device on I2C port 1
    i2cdetect -y 1 # get address for device on I2C port 1
    ```
    Your result should be similar to below.  Make note of your BMP280's address.
    <img src="images/bmp280_software_validation.png" alt="Validate BMP280 Wiring to Pi" width="600" />

1. Update the course repository on your Pi 
[Updating local course repository from GitHub](../references/Tips_and_Tricks.md)
    ```
    cd /home/pi/seneca-prg550-2022-spring
    git pull
    ```
1. Copy BMP280 test file to your working directory
    ```
    mkdir /home/pi/workspace/project
    cp /home/pi/seneca-prg550-2022-spring/project/bmp280_test.py /home/pi/workspace/project/
    ```
1. Run the test file to verify your BMP280 is capturing data.  Your output should be similar to below.  Use `ctrl-c` to stop the program
    ```
    cd /home/pi/workspace/project
    python3 bmp280_test.py
    ```
    Program Output
    ```
    /home/pi/workspace/project >python3 bmp280_test.py

    Temperature: 29.3961 C
    Pressure: 987.4638 hPa
    Altitude = 78.9667 meters

    Temperature: 29.3910 C
    Pressure: 987.4677 hPa
    Altitude = 78.4086 meters
    ```


## Rapsberry Pi Header Pinouts
This table shows the Pi pin header numbers and their names

| Name | HLeft| HRight | Name |
|----:|:-----:|:-----:|:-----|
|3.3v DC Power | 1 | 2 | 5v DC Power |
|GPIO02 (SDA1, I2C) | 3 | 4 | 5v DC Power |
|GPIO03 (SCL1, I2C) | 5 | 6 | Ground |
|GPIO04 (GPIO_GCLK) | 7 | 8 | GPIO14 (TXD0) |
|Ground | 9 | 10 | GPIO15 (RXD0) |
|GPIO17 (GPIO_GEN0) | 11 | 12 | GPIO18 (GPIO_GEN1) |
|GPIO27 (GPIO_GEN2) | 13 | 14 | Ground |
|GPIO22 (GPIO_GEN3) | 15 | 16 | GPIO23 (GPIO_GEN4) |
|3.3v DC Power | 17 | 18 | GPIO24 (GPIO_GEN5) |
|GPIO10 (SPI_MOSI) | 19 | 20 | Ground |
|GPIO09 (SPI_MISO) | 21 | 22 | GPIO25 (GPIO_GEN6) |
|GPIO11 (SPI_CLK) | 23 | 24 | GPIO08 (SPI_CE0_N) |
|Ground | 25 | 26 | GPIO07 (SPI_CE1_N) |
|ID_SD (I2C ID EEPROM) | 27 | 28 | ID_SC (I2C ID EEPROM) |
|GPIO05 | 29 | 30 | Ground |
|GPIO06 | 31 | 32 | GPIO12 | 
|GPIO13 | 33 | 34 | Ground |
|GPIO19 | 35 | 36 | GPIO16 | 
|GPIO26 | 37 | 38 | GPIO20 | 
|Ground | 39 | 40 | GPIO21 |


## Raspberry Pi Hardware commands
```
pinout
```



[^1]: https://learn.adafruit.com/assets/93031
