# Importing the modules we need
from tkinter import *
from tkinter import ttk
import threading

# Create a Class for the Tkinter window
class win:
    # This function below automatically executes when the class is called
    def __init__(self, mat, web):
        # Creating a window
        self.root = Tk()
        # Title for the window
        self.root.title("Measuring humidity and Temperature using DHT22 sensor")
        # Size of the window in pixels
        self.root.geometry("300x300")
        # Creating the button which runs matplotlib, threading is not required as the function doesn't use a while loop
        self.btn1 = ttk.Button(self.root, text="Open Matplotlib graph", command=mat)
        self.btn1.grid(row=0, column=0, sticky=NSEW)
        # Creating the button which runs flask application, it must be threaded as it has a while loop in it
        self.btn2 = ttk.Button(self.root, text="Open graph on webbrowser", command=threading.Thread(target=web).start)
        self.btn2.grid(row=1, column=0, sticky=NSEW)
        # This makes the window stay all the time and not just closing within a second
        self.root.mainloop()
