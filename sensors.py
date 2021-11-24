import adafruit_dht, time, sys, os, itertools as it
from board import *

time_values = []
humidity_data = []
temperature_data = []

dht22 = adafruit_dht.DHT22(D4, use_pulseio=False)


def data():
    global humidity_data, temperature_data, humidityAverage, temperatureAverage, dht22, time_values
    while True:
        try:
            humidity  = dht22.humidity
            temperature = dht22.temperature
            index = it.count()
            if temperature == None:
                print("Unable to get temperature")
                temperature_data.append(temperature_data[-1])
            else:
                temperature_data.append(temperature)
                temperatureAverage = sum(temperature_data) / len (temperature_data)
            if humidity == None:
                print("Unable to get humidity")
                humidity_data.append(humidity_data[-1])
            else:
                humidity_data.append(humidity)
                humidityAverage = sum(humidity_data) / len (humidity_data)
            time_values.append(next(index))      
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(f"Ignored error: {e}")
            continue
        time.sleep(1)
