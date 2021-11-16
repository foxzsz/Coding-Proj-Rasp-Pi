import Adafruit_DHT
import time


humidity = 0
count = 0
humidityminute =  []
temperatureminute = []


def MinuteAverageCalculator():
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 4
    while True:
        if count == 60:
            humdityaverage = sum(humidityminute) / len(humidityminute)
            temperatureaverage = sum(temperatureminute) / len(temperatureminute)
            count = 0
            minutearr.clear()
            temperatureminute.clear()
        else:
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            humidityminute.append(humidity)
            temperatureminute.append(temperature)
            count +=1
            time.sleep(1)

        

""" def HumidityUpdater():
    global humidity
    try:
        DHT_SENSOR = Adafruit_DHT.DHT22
        DHT_PIN = 4
    except Exception:
        print("Error connecting to Humdity sensor")
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
           print(" Updated values Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        else:
           print("Failed to retrieve data from humidity sensor")
        time.sleep(1) """