import json, time, threading
from datetime import datetime
from flask import Flask, Response, render_template
from sensors import *

def web():
    application = Flask(__name__)
    #random.seed()

    @application.route('/')
    def index():
        return render_template('index.html')

    @application.route('/chart-data')
    def chart_data():
        def update_chart_data():
            while True:
                equation = "Equation: Humidity = Temperature × " + round(float(humidityAverage / temperatureAverage), 2)
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

    application.run(host="0.0.0.0")