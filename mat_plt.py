import threading, matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sensors import *

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