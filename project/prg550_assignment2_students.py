# Dora Lee, 2022
# This file contains a set of helper functions for PRG550 assignment 2

import requests
import pandas as pd

import pandas as pd
import requests
import re

import time
import board
import adafruit_bmp280
import math


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump, load

prg550_weather_2labels = {
    'Mostly Cloudy':'NoRain', 
    'Cloudy':'NoRain', 
    'Fog':'NoRain', 
    'Moderate Rain Showers':'Rain', 
    'Thunderstorms':'Rain',
    'Thunderstorms,Moderate Rain Showers':'Rain', 
    'Rain':'Rain', 
    'Rain Showers':'Rain', 
    'Rain Showers,Fog':'Rain', 
    'Rain,Fog':'Rain',
    'Mainly Clear':'NoRain', 
    'Clear':'NoRain',
    'Moderate Rain,Fog':'Rain',
    'Thunderstorms,Heavy Rain Showers':'Rain',
    'Drizzle':'Rain',
}    


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
    
    

def data_collection(stationID, climateID, year, month, day, timeframe_type=1):
    """
        hourly data: timeframe_type=1
        daily data: timeframe_type=2
        monthly data: timeframe_type=3
    """
    url_base = "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?"
    url_hourly = "{url_base}format=csv&stationID={stationID}&Year={year}&Month={month:02d}&Day={day:02d}&timeframe=1".format(url_base=url_base, stationID=stationID, year=year, month=month, day=day)
    url_daily = "{url_base}format=csv&stationID={stationID}&Year={year}&Month={month:02d}&Day={day:02d}&timeframe=2".format(url_base=url_base, stationID=stationID, year=year, month=month, day=day)
    url_monthly = f"{url_base}format=csv&stationID={stationID}&Year={year}&Month={month:02d}&timeframe=3".format(url_base=url_base, stationID=stationID, year=year, month=month)

    download_date_str = f"{year}-{month:02d}-{day:02d}"

    if timeframe_type==1:
        url = url_hourly
    elif timeframe_type==2:
        url = url_daily
    elif timeframe_type==3:
        url = url_monthly
    else:
        raise Exception("data_collection: invalid timeframe_type")

    try:
        response = requests.get(url)    
    except:
        print(f"data_collection: error with climate.weather.gc.ca API request: {url}")

    try:
        data_download_filepath = f'environment_canada_station_data_{stationID}_{climateID}_{download_date_str}.csv'
        with open(data_download_filepath, 'w') as f:
            f.write(response.content.decode("utf-8"))
    except:
        print(f"data_collection: error writing data to file {data_download_filepath} ")

    data_raw_df = pd.read_csv(data_download_filepath)    
    return data_raw_df


def data_clean_prep(data_raw_df):
    feature_target_fields = ['Temp', 'StnPress', 'DewPointTemp_fix', 'RelHum_fix', 'Visibility_fix', 'Hmdx_fix', 'WindSpd_fix', 'Weather_fix', 'PRG550_2labels']

    data_clean_df = data_raw_df.copy()

    # remove special characters from column names
    data_clean_df.columns = [clean_column_names(c) for c in data_clean_df.columns]

    # fill in missing values
    data_clean_df['Weather_fix'] = data_clean_df['Weather'].fillna(method='ffill') # forward fill NA's (previous hour's observation passes into the next)
    data_clean_df['Weather_fix'] = data_clean_df['Weather_fix'].fillna(method='bfill') # forward fill NA's (previous hour's observation passes into the next)
    data_clean_df['Hmdx_fix'] = data_clean_df['Hmdx'].fillna(method='ffill') # forward fill NA's (previous hour's observation passes into the next)
    data_clean_df['Hmdx_fix'] = data_clean_df['Hmdx_fix'].fillna(method='bfill') # forward fill NA's (previous hour's observation passes into the next)    
    data_clean_df['WindSpd_fix'] = data_clean_df['WindSpd'].fillna(method='ffill') # forward fill NA's (previous hour's observation passes into the next)
    data_clean_df['WindSpd_fix'] = data_clean_df['WindSpd'].fillna(method='bfill') # forward fill NA's (previous hour's observation passes into the next)
    data_clean_df['DewPointTemp_fix'] = data_clean_df['DewPointTemp'].fillna(method='ffill') # forward fill NA's (previous hour's observation passes into the next)
    data_clean_df['DewPointTemp_fix'] = data_clean_df['DewPointTemp'].fillna(method='bfill') # forward fill NA's (previous hour's observation passes into the next)
    data_clean_df['RelHum_fix'] = data_clean_df['RelHum'].fillna(method='ffill') # forward fill NA's (previous hour's observation passes into the next)
    data_clean_df['RelHum_fix'] = data_clean_df['RelHum'].fillna(method='bfill') # forward fill NA's (previous hour's observation passes into the next)
    data_clean_df['Visibility_fix'] = data_clean_df['Visibility'].fillna(method='ffill') # forward fill NA's (previous hour's observation passes into the next)
    data_clean_df['Visibility_fix'] = data_clean_df['Visibility'].fillna(method='bfill') # forward fill NA's (previous hour's observation passes into the next)

    # create target weather labels
    data_clean_df['PRG550_2labels'] = data_clean_df['Weather_fix'].apply(lambda row: prg550_weather_2labels[row])

    return data_clean_df[feature_target_fields].copy()



def clean_column_names(column_name):
    """
    remove special characters from column names
    """
    col_stage1 = re.sub('\(.*\)','',column_name) # remove parts of string enclosed in brackets
    col_stage2 = re.sub('[. /]','',col_stage1) # remove '.', ' ', '/' from string
    return col_stage2



def model_train(data_clean_df, features, target, model_filename=None,
    random_state=None):
    """model_train [summary]

    Parameters
    ----------
    data_clean_df : [pd.DataFrame]
        dataframe with cleaned data
    features : [list]
        list of columns to use as feature
    target : [string]
        field name to use as label
    """

    df_features = data_clean_df[features]
    df_target = data_clean_df[target]


    # split data into train and test
    percentage_for_testing = 0.2 # 20% data for testing, 80% for training
    df_features_train, df_features_test, df_target_train, df_target_test = train_test_split(
        df_features
        , df_target
        , test_size=percentage_for_testing
        , random_state=random_state)

    # instantiate and train logistic regression model
    clf = LogisticRegression(random_state=0)
    clf.fit(df_features_train, df_target_train)

    dump(clf, model_filename) 


def model_load(model_filename=None):
    if model_filename is None:
        raise Exception("model_load: must provide model filename")
    
    clf = load(model_filename) 
    return clf