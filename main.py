import json
import time
from datetime import datetime
from sensors import *
import threading

from flask import Flask, Response, render_template

application = Flask(__name__)



@application.route('/')
def index():
    return render_template('index.html')


@application.route('/chart-data')
def chart_data():
    def update_chart_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': humidity})
            yield f"data:{json_data}\n\n"
            time.sleep(10)

    return Response(update_chart_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    threading.Thread(target=HumidityUpdater).start()
    application.run(debug=True, threaded=True)