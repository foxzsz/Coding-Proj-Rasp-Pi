import json, time, threading
# import random
import sys,os
from datetime import datetime
from flask import Flask, Response, render_template

application = Flask(__name__)

import adafruit_dht, time
from board import *

humidity_data = []
temperature_data = []
humidityAverage = 0
temperatureAverage = 0
SENSOR_PIN = D4
dht22 = adafruit_dht.DHT22(SENSOR_PIN, use_pulseio=False)

def data():
    global humidity_data, temperature_data, humidityAverage, temperatureAverage, dht22
    while True:
        try:
            humidity  = dht22.humidity
            temperature = dht22.temperature
            print(temperature)
            print(humidity)
            if temperature == None:
                print("Unable to get temperature")
            else:
                temperature_data.append(temperature)
                temperatureAverage = sum(temperature_data) / len (temperature_data)
            if humidity == None:
                print("Unable to get humidity")
            else:
                humidity_data.append(humidity)
                humidityAverage = sum(humidity_data) / len (humidity_data)
            time.sleep(1)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print(f"Ignored error: {e}")
            time.sleep(1)
            continue


# random.seed()

@application.route('/')
def index():
    return render_template('index.html')


@application.route('/chart-data')
def chart_data():
    def update_chart_data():
        global humidityAverage,temperatureAverage,humidity_data
        while True:
            equation = "Equation: Humidity = Temperature × " + str(humidityAverage / temperatureAverage)
            """
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'humidity': random.randint(1, 50), 'temperature': random.randint(1, 50)})
            yield f"data:{json_data}\n\n"
            """
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'humidity': humidity_data[-1], 'temperature': temperature_data[-1], 'equation': equation})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(update_chart_data(), mimetype='text/event-stream')

threading.Thread(target=data).start()
application.run(host="0.0.0.0",debug=True, threaded=True)



