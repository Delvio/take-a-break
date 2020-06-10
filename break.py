import time
import webbrowser
import tkinter
from tkinter import messagebox
ideal_breaks = 3
breaks_taken = 0

while (breaks_taken< ideal_breaks):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=5qap5aO4i9A")
    
    time.sleep(60*15)
    #increase the brakes taken
    breaks_taken += 1
    #tkinter
    root = tkinter.Tk()
    #hide the tkinter window
    root.withdraw()
    # Message Box
    if breaks_taken>=2:
        messagebox.showinfo("Break Time", "It's time for you to take a another break ")
    else:
        messagebox.showinfo("Break Time", "It's time for you to take a break")


