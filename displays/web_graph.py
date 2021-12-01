# Importing the needed modules
import json, threading, webbrowser, socket
from datetime import datetime
from flask import Flask, Response, render_template
from .sensors import *

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
                equation = "and Equation of Humidity in terms of temperature is: Humidity = Temperature × " + str(round((humidityAverage / temperatureAverage), 1))

                # Declare the max and min value of humidity and temperature
                humidity = "Maximum humidity = " + str(max(humidity_data)) + ", Minimum humidity = " + str(min(humidity_data))
                temperature = "Maximum temperature = " + str(max(temperature_data)) + ", Minimum temperature = " + str(min(temperature_data))

                paragraph = humidity + ', ' + temperature + ', ' + equation

                # Create json data with the humidity and temperature data(JavaScript Object Notation) so the browser can use it.
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%H:%M:%S'), 'humidity': humidity_data[-1], 'temperature': temperature_data[-1], 'paragraph': paragraph})
                # Yield the data Definition: "The yield statement suspends function's execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left" (https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)
                yield f"data:{json_data}\n\n"
                # pause for 1 second
                time.sleep(60)
        # Send an event to the browser
        return Response(update_chart_data(), mimetype='text/event-stream')
    
    # Check the os of the device if it is windows or mac os x
    if sys.platform == "win32" or "darwin":
        # Get the local ip address and open it automatically by webbrowser
        ip = "http://" + socket.gethostbyname(socket.gethostname()) + ":5000"
    # Note: This is just used to test at home and me and can have different os.
    else:
        # This is the url to open on raspberry pi
        ip = "http://0.0.0.0:5000/"
    webbrowser.open(ip)

    # Threading is used to run many functions and loops at a time. This data function is used from sensors.py
    threading.Thread(target=data).start()
    #threading.Thread(target=fakedata).start()


    # Run the application, if run on the ip address 0.0.0.0 other people can access the website in their browser
    application.run(host="0.0.0.0")
