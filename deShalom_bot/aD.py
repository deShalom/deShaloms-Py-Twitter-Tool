import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from module1 import tweet
import time
import schedule

path = "RobotSmall.png"
 
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # - Creating background.
        canvas = tk.Canvas(self, height=300, width=400, bg="#8ca0de", highlightthickness=0)
        canvas.pack()
        # - Implementing the menu bar.
        buttonFrame = tk.Frame(canvas, bg="#7651b5")
        buttonFrame.place(relwidth=1, relheight=0.2, relx=0.0, rely=0.1)
        # - Adding buttons to the menu bar.
        tk.Button(buttonFrame, bg="#7651b5", borderwidth=0, text="Settings", command=lambda: master.switch_frame(PageOne)).place(relx=0.5, rely=0.75, anchor=CENTER)
        tk.Button(buttonFrame, bg="#7651b5", borderwidth=0, text="Home", command=lambda: master.switch_frame(PageOne)).place(relx=0.35, rely=0.75, anchor=CENTER)
        tk.Button(buttonFrame, bg="#7651b5", borderwidth=0, text="Keys", command=lambda: master.switch_frame(PageOne)).place(relx=0.65, rely=0.75, anchor=CENTER)
        # - Creating and saving refence to the logo.
        img = ImageTk.PhotoImage(Image.open(path))
        self.photo = img
        # - Creating the light shaded blue panel.
        frame = tk.Frame(self, bg="#7081b5")
        # - Implementing the image.
        panel = Label(frame, image = self.photo, bg="#7081b5")
        panel.place(relwidth=0.2, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)
        frame.place(relwidth=1, relheight=0.2)
        # - Adding the input field and button.
        e1 = tk.Entry(canvas)
        e1.place(relx=0.5, rely=0.5, anchor=CENTER)
        tk.Button(canvas, bg="#7651b5", borderwidth=1, text="Tweet", command=lambda:tweet(e1.get())).place(relx=0.75, rely=0.5, anchor=CENTER)
                 

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
