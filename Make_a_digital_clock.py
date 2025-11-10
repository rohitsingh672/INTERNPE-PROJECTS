# Importing tkinter module for GUI development
import tkinter as tk

# Importing strftime function to get the current time in a formatted string
from time import strftime

# Creating the main application window
root = tk.Tk()

# Setting the title of the window
root.title("Digital Clock")

# Defining the function that updates the time on the label
def time():

    # Getting the current time in the format: Hours:Minutes:Seconds AM/PM newline Date
    string = strftime('%I:%M:%S %p \n %D')

    # Updating the text of the label with the current time
    label.config(text=string)

    # Scheduling the 'time' function to run again after 1000 milliseconds (1 second)
    label.after(1000, time)

# Creating a label widget with a specific font, background, and text color
label = tk.Label(root, font=('calibri', 50, 'bold'), background='green', foreground='black')

# Placing the label in the center of the window
label.pack(anchor='center')

# Calling the time function for the first time to start the clock
time()

# Running the Tkinter event loop (keeps the window open and responsive)
root.mainloop()
