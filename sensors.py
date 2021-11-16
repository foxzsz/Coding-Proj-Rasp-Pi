import Adafruit_DHT, time

count = 0
humidityMinute =  []
temperatureMinute = []

def MinuteAverageCalculator():
    DHT_SENSOR = Adafruit_DHT.DHT22
    #DHT_PIN = 4
    global count, humidityAverage, temperatureAverage
    while count<=20:
        #humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        humidity, temperature = DHT_SENSOR.humidity, DHT_SENSOR.temperature
        humidityMinute.append(humidity)
        temperatureMinute.append(temperature)
        count +=1
        time.sleep(1)
        humidityAverage = sum(humidityMinute) / len(humidityMinute)
        temperatureAverage = sum(temperatureMinute) / len(temperatureMinute)
