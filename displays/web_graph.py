import json, time, threading
from datetime import datetime
from flask import Flask, Response, render_template
from .sensors import *


## Function which initiates the flask app
def web():
    application = Flask(__name__)

    ## Used for testing
    #random.seed()
    

    ## Create application route which returns the html template index.html from the /templates dir
    @application.route('/')
    def index():
        return render_template('index.html')


    ## This is used to update the data on the users browser, using Server-sent events the webserver will send the new data to the user  to update their graph
    @application.route('/chart-data')
    def chart_data():
        def update_chart_data():
            ## Sends data to the users browser
            while True:
                ## Create the equation using the averages
                equation = "Equation: Humidity = Temperature × " + round(float(humidityAverage / temperatureAverage), 2)

                ## Used for testing
                """
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%H:%M:%S'), 'humidity': random.randint(1, 50), 'temperature': random.randint(1, 50)})
                yield f"data:{json_data}\n\n"
                """
                ## Create json data (JavaScript Object Notation) so the browser can use it
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%H:%M:%S'), 'humidity': humidity_data[-1], 'temperature': temperature_data[-1], 'equation': equation})
                ## Yield the data Definition: "The yield statement suspends function's execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left" (https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)
                yield f"data:{json_data}\n\n"
                
                time.sleep(1)
        ## Send an event to the browser
        return Response(update_chart_data(), mimetype='text/event-stream')
    
    ## Run the application, if run on the ip address 0.0.0.0 other people can access the website in their browser
    application.run(host="0.0.0.0")