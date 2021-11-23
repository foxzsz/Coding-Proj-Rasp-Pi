import adafruit_dht, time, sys, os
from board import *

humidity_data = []
temperature_data = []
dht22 = adafruit_dht.DHT22(D4, use_pulseio=False)

def data():
    global humidity_data, temperature_data, humidityAverage, temperatureAverage, dht22
    while True:
        try:
            humidity  = dht22.humidity
            temperature = dht22.temperature
            if temperature and humidity != None:
                temperature_data.append(temperature)
                humidity_data.append(humidity)
                temperatureAverage = sum(temperature_data) / len (temperature_data)
                humidityAverage = sum(humidity_data) / len (humidity_data)       
            else:
                print("DHT sensor not working")         
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(f"Ignored error: {e}")
            continue
        time.sleep(1)
