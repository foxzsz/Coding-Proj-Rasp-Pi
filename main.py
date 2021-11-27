# Importing our own files
from time import sleep
from displays import mat_plt, web_graph
import threading, displays.templates.tk as tk
from sensors import *

# Run the class window from tk file and pass the commands mat(which is used for graphing on matplotlib) and web(which is used to graph on a webpage) to the buttons of the window
window = tk.win(mat_plt.mat, web_graph.web)
# Threading is used to run many functions and loops at a time. This data function is used from sensors.py
threading.Thread(target=data).start()
