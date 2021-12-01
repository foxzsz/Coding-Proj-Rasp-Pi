# Importing the needed modules
import threading, matplotlib.pyplot as plt, itertools as it
from matplotlib.animation import FuncAnimation
from .sensors import *

# Matplotlib graph function
def mat():

    # Threading is used to run many functions and loops at a time. This data function is used from sensors.py
    threading.Thread(target=data).start()
    #threading.Thread(target=fakedata).start()

    def animate(i):
        # Plotting a line graph using the values from sensors.py
        plt.plot(time_values, humidity_data, '-b', label='humidity')
        plt.plot(time_values, temperature_data, '-r',  label='temperature')
        # Creating a scatter plot so people can know the data values
        plt.scatter(time_values, humidity_data, c='blue')
        plt.scatter(time_values, temperature_data, c= 'red')
        # The legend location in the window is upper left
        plt.gca().legend(('Humidity', 'Temperature'), loc="upper left")
    # Animate the graph using funcanimation and set the interval as 60000ms(milliseconds)
    live = FuncAnimation(plt.gcf(), animate, interval=60000)

    plt.xlabel("time(seconds)")
    plt.ylabel("humidity(%), temperature(°C)")
    # Display the window
    plt.show()
