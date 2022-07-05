import time
import board
import adafruit_bmp280
from datetime import datetime


def main():

   i2c = board.I2C()
   bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c) # use default address
   bmp280.sea_level_pressure = 100.85  # set on 22/07/05 @ 15h20, sea level pressure in Toronto, in hPa

   # put code here to create data file BMP280_data_collection_YYYYmmdd-HH:MM:SS.csv

   # pseudo code to help you get started

   # use string formatting and datetime functions to create file name 
   # open file for writing
   # loop to capture 100 data points
   #    1. read temperature, pressure, altitude from bmp280
   #    2. format data into csv
   #    3. write one line of data to file
   # close file   

if __name__ == "__main__" :
   main()