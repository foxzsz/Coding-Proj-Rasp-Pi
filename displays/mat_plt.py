import threading, matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from .sensors import *

## Matplotlib graph function
def mat():
    threading.Thread(target=data).start()
    def animate(i):

        ## Function for updating the data on the graph
        plt.cla()
        plt.plot(time_values, humidity_data, label='humidity')
        plt.plot(time_values, temperature_data, label='temperature')
        plt.scatter(time_values, humidity_data)
        plt.scatter(time_values, temperature_data)
        plt.legend(loc="upper left")
    ## Create graph
    live = FuncAnimation(plt.gcf(), animate, interval=1000)
    plt.tight_layout()
    plt.xlabel("time(seconds)")
    plt.ylabel("humidity(%), temperatre(°C)")
    plt.show()
