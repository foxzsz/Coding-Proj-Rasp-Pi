import Adafruit_DHT, time

humidity_data = []
temperature_data = []

def data():
    global humidity_data, temperature_data, humidityAverage, temperatureAverage
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
        humidity_data.append(round(humidity, 2))
        temperature_data.append(round(temperature, 2))
        humidityAverage = sum(humidity_data) / len(humidity_data)
        temperatureAverage = sum(temperature_data) / len(temperature_data)
        time.sleep(1) 
