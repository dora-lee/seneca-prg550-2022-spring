import time
import board
import adafruit_bmp280

i2c = board.I2C()
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c) # use default address
# bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76) # uncomment if needing explicit address
# bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77) # uncomment if needing explicit address

bmp280.sea_level_pressure = 100.85  # set on 22/07/05 @ 15h20, sea level pressure in Toronto, in hPa

while True:
   print("\nTemperature: %0.4f C" % bmp280.temperature)
   print("Pressure: %0.4f hPa" % bmp280.pressure)
   print("Altitude = %0.4f meters" % bmp280.altitude)
   time.sleep(2)
