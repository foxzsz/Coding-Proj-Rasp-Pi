import json, time, random
from datetime import datetime
#from sensors import *
#import threading
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
        while ls_counter <= 20:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': random.randint(0, 50)})
            yield f"data:{json_data}\n\n"
            """
            json_data_humidity = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': humidityminute[ls_counter]})
            yield f"data:{json_data}\n\n"
            json_data_temperature = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': temperatureminute[ls_counter]})
            yield f"data:{json_data}\n\n"
            """
            ls_counter += 1
            time.sleep(1)

    return Response(update_chart_data(), mimetype='text/event-stream')

#threading.Thread(target=MinuteAverageCalculator).start()
application.run(debug=True, threaded=True)