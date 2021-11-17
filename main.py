import json, time, random
from datetime import datetime
from sensors import *
import threading
from flask import Flask, Response, render_template

application = Flask(__name__)
random.seed()

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/chart-data')
def chart_data():
    def update_chart_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'humidity': humidity, 'temperature': temperature})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(update_chart_data(), mimetype='text/event-stream')

threading.Thread(target=MinuteAverageCalculator).start()
application.run(debug=True, threaded=True)