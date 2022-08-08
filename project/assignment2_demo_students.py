from joblib import dump, load
import pandas as pd
import numpy as np
import time
import board
import adafruit_bmp280


from datetime import datetime
from joblib import dump, load


def bmp_initialize(device_address=0x77):
    """
    initialize i2c connection with default address (0x77)
        alternate address 0x76
    
    https://docs.circuitpython.org/projects/bmp280/en/latest/api.html
    """
    i2c = board.I2C()
    bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=device_address)  

    return bmp280

def bmp_read_values(bmp280_i2c, display_values=True):
    # read values from BMP280 and assign to variables
    bmp_pressure = bmp280_i2c.pressure
    bmp_altitude = bmp280_i2c.altitude
    bmp_temperature = bmp280_i2c.temperature

    if display_values==True:
        print("\nTemperature: %0.4f °C" % bmp_pressure)
        print("Pressure: %0.4f hPa" % bmp_pressure)
        print("Altitude = %0.4f meters" % bmp_pressure)
    return( bmp_temperature, bmp_pressure, bmp_altitude)

def bmp_pressure_offset_prompt():
    try:
        pressure_offset = float(input(f"Enter offset to use for measured pressure in kPa (default=0): "))
    except ValueError:
        pressure_offset = 0.0
    return pressure_offset
    
def save_measured_data(realtime_data):
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!! your code here to save data into csv file


def main():

    bmp280 = bmp_initialize() # instantiate bmp280 connection
    
    model_filename = 'balanced_data_environment_canada_logistic_regression_classifier.joblib'
    clf = load(model_filename) 

    target_label_dict = {0: 'NoRain', 1:'Rain'} # map 0/1 to NoRain/Rain
    
    pressure_offset = bmp_pressure_offset_prompt()

    realtime_data = [] # list to save measured BMP280 data and model prediction
    for idx in range(0,120): # run for 1 minutes
        measurement_time = datetime.now()
        temperature, pressure, altitude = bmp_read_values(bmp280, display_values=False)
        pressure_kpa = pressure/10 # pressure reading from bmp280 is in hPa; convert hPa to kPa
        pressure_kpa += pressure_offset # use offset to shift data so that temperature can have more effect
        features = np.array([temperature, pressure_kpa]).reshape(1,2)
        prediction = clf.predict(features)[0]
        prediction_label = target_label_dict[prediction]
        print(f"{temperature}, {pressure_kpa} --> Prediction: {prediction}({prediction_label})")
        
        realtime_data.append([measurement_time, temperature, pressure_kpa, prediction, prediction_label])
        time.sleep(0.15) # sleep for 0.5 seconds
    
    save_measured_data(realtime_data)

if __name__ == "__main__" :
   main()