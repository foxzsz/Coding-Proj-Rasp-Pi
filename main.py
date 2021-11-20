import json, time, random, threading
from datetime import datetime
from sensors import *
from flask import Flask, Response, render_template

application = Flask(__name__)
random.seed()

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/chart-data')
def chart_data():
    def update_chart_data():
        ls_counter = 0
        while True:
            equation = "Equation: Humidity = Temperature × " + str(humidityAverage/ temperatureAverage)
            """
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'humidity': random.randint(1, 50), 'temperature': random.randint(1, 50)})
            yield f"data:{json_data}\n\n"
            """
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'humidity': humidity_data[ls_counter], 'temperature': temperature_data[ls_counter], 'equation': equation})
            yield f"data:{json_data}\n\n"
            ls_counter += 1
            
            time.sleep(1)

    return Response(update_chart_data(), mimetype='text/event-stream')

threading.Thread(target=data).start()
application.run(debug=True, threaded=True)