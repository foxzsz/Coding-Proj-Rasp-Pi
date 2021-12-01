import time, sys, os, itertools as it
from board import *
import adafruit_dht
import random

# Define Values
humidity_data = []
temperature_data = []
time_values = []
index = it.count()

# Create dht22 object
dht22 = adafruit_dht.DHT22(D4, use_pulseio=False)

# Main function for getting the data
#"""
def data():
    global humidity_data, temperature_data, dht22, time_values,index
    while True:
        # A try and except is needed for this function, this is because the DHT 22 returns a lot of errors and error handling is neccesary here to keep it running
        
        try:
            # Get the values
            humidity  = dht22.humidity
            temperature = dht22.temperature

            # The dht22 also commonly returns "None" as the temperature or humidity value. To not cause any error we have to make an if statement, an error would happen when there is no data in the list and it tries to calculate the average
            if temperature == None:
                print("Unable to get temperature")
            else:
                temperature_data.append(temperature)
            if humidity == None:
                print("Unable to get humidity")
            else:
                humidity_data.append(humidity)
            time_values.append(next(index))
        except Exception as e:
            # This is not really neccesary however using this it allows us to see exactly which line is causing the error
            exc_type, exc_obj, exc_tb = sys.exc_info()
            f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, f_name, exc_tb.tb_lineno)
            print(f"Ignored error: {e}")
            continue
        time.sleep(60)
#"""

# This function is used to test if all the files are working so we can also test it without the DHT 22 Sensor
def fakedata():
    global humidity_data, temperature_data, dht22, time_values,index
    while True:
        humidity = random.randint(1, 50)
        temperature = random.randint(1, 50)
        temperature_data.append(temperature)
        humidity_data.append(humidity)
        time_values.append(next(index))
        time.sleep(1)
