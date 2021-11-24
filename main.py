import json, time, threading, templates.tk
from datetime import datetime
from sensors import *
from flask import Flask, Response, render_template
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mat():
    #time_values = []
    #humidity_data = []
    #temperature_data = []
    #index = count()
    def animate(i):
        #time_values.append(next(index))

        #humidity_data.append(random.randint(1, 50))
        #temperature_data.append(random.randint(1, 50))
        plt.cla()
        plt.plot(time_values, humidity_data, label='humidity')
        plt.plot(time_values, temperature_data, label='temperature')
        plt.scatter(time_values, humidity_data)
        plt.scatter(time_values, temperature_data)
        plt.legend(loc="upper left")
    live = FuncAnimation(plt.gcf(), animate, interval=1000)
    plt.tight_layout()
    plt.xlabel("time(seconds)")
    plt.ylabel("humidity(%), temperatre(°C)")
    plt.show()
    threading.Thread(target=data).start()

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

    threading.Thread(target=data).start()
    application.run(host="0.0.0.0")
window = templates.tk.win(mat, web)
