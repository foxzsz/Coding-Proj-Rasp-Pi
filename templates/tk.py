from tkinter import *
from tkinter import ttk
import threading

class win:
    def __init__(self, mat, web):
        self.root = Tk()
        self.root.title("Measuring humidity and Temperature using DHT22 sensor")
        self.root.geometry("500x500")
        self.btn1 = ttk.Button(self.root, text="Open Matplotlib graph", command=mat)
        self.btn1.grid(row=0, column=0, sticky=NSEW)
        self.btn2 = ttk.Button(self.root, text="Open graph on webbrowser", command=threading.Thread(target=web).start)
        self.btn2.grid(row=1, column=0, sticky=NSEW)
        self.root.mainloop()
