import Adafruit_DHT, time

count = 0
humidityminute =  []
temperatureminute = []

def MinuteAverageCalculator():
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 4
    global count, humdityaverage, temperatureaverage
    while count<=20:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        humidityminute.append(humidity)
        temperatureminute.append(temperature)
        count +=1
        time.sleep(1)
        humdityaverage = sum(humidityminute) / len(humidityminute)
        temperatureaverage = sum(temperatureminute) / len(temperatureminute)
