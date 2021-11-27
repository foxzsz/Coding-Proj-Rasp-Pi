# Importing the needed modules
import json, threading, webbrowser
from datetime import datetime
from flask import Flask, Response, render_template
from sensors import *

# Function which initiates the flask app
def web():
    application = Flask(__name__)

    # Used for testing:
    #random.seed() 

    # Create application route which returns the html template index.html from the templates/ dir
    @application.route('/')
    def index():
        return render_template('index.html')
        

    # This is used to update the data on the users browser, using Server-sent events the webserver will send the new data to the user  to update their graph
    @application.route('/chart-data')
    def chart_data():
        def update_chart_data():
            while True:
                # Create the equation using the averages
                humidityAverage = sum(humidity_data) / len(humidity_data)
                temperatureAverage = sum(temperature_data) / len(temperature_data)
                equation = "Equation: Humidity = Temperature × " + str(humidityAverage / temperatureAverage)

                # Create json data with the humidity and temperature data(JavaScript Object Notation) so the browser can use it.
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%H:%M:%S'), 'humidity': humidity_data[-1], 'temperature': temperature_data[-1], 'equation': equation})
                # Yield the data Definition: "The yield statement suspends function's execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left" (https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)
                yield f"data:{json_data}\n\n"
                # pause for 1 second
                time.sleep(1)
        # Send an event to the browser
        return Response(update_chart_data(), mimetype='text/event-stream')
    
    #threading.Thread(target=data).start()

    #webbrowser.open_new('http://192.168.0.43:5000/')
    # Run the application, if run on the ip address 0.0.0.0 other people can access the website in their browser
    application.run(host="0.0.0.0")
    
