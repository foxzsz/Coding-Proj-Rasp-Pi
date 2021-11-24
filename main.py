from .displays import *
import templates.tk as tk

## Total lines of code: 248


## This will start a thread / subproccess which will update the data every second, this is required for thw website and the graph
threading.Thread(target=data).start()


## Create a new Tkinter window and use the functions as the paramaters
window = tk.win(mat, web)
