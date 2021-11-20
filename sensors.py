import adafruit_dht, time
from board import *

humidity_data = []
temperature_data = []

def data():
    global humidity_data, temperature_data, humidityAverage, temperatureAverage
    dht22 = adafruit_dht.DHT22(D4, use_pulseio=False)
    while True:
        humidity  = round(dht22.humidity, 2)
        temperature = round(dht22.temperature, 2)
        humidity_data.append(humidity)
        temperature_data.append(temperature)
        humidityAverage = sum(humidity_data) / len(humidity_data)
        temperatureAverage = sum(temperature_data) / len(temperature_data)
        time.sleep(1)