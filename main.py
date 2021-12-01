# Importing our own files
from displays import mat_plt, web_graph
import displays.templates.tk as tk

# Run the class window from tk file and pass the commands mat(which is used for graphing on matplotlib) and web(which is used to graph on a webpage) to the buttons of the window
window = tk.win(mat_plt.mat, web_graph.web)
