import tweepy
import time
import schedule
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

#---- Variables
print("Debug - Launched")
path = "RobotSmall.png"

#---- GUI implementation below
root = tk.Tk()
root.configure(background="#8ca0de")
root.title("deShalom's AstroMech Droid")

canvas = tk.Canvas(root, height=300, width=400, bg="#8ca0de", highlightthickness=0)
canvas.pack()

#----Header
img = ImageTk.PhotoImage(Image.open(path))

frame = tk.Frame(root, bg="#7081b5")
panel = Label(frame, image = img, bg="#7081b5")
panel.place(relwidth=0.2, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)
frame.place(relwidth=1, relheight=0.2)

root.mainloop()


