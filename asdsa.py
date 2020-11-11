import os
from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.scrolledtext as st
from main2 import *

LARGEFONT = ("Verdana", 35, "bold")

myFont = ("Helvetica", 50)

backgroundColor = '#350f58'
btncolor = '#884dbc'

name_var=tk.StringVar()

def submit():
    name=Page1.applyname.get()
    print("The username is " + name)
    name_var.set("")

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Sim League")
        self.geometry("1500x720")
        self.iconbitmap("poro-icon.ico")
        self.config(background=backgroundColor)
        self.resizable(width=False, height=False)


        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # first window frame startpage


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background=backgroundColor)
        singleplayerbutton = tk.Button(self, bg=btncolor, font=myFont, highlightthickness=0, bd='0', text="START",
                                       command=lambda: controller.show_frame(Page1))
        singleplayerbutton.place(relx=0.5, rely=0.5, relwidth=0.40, relheight=0.20, anchor=CENTER)

    # second window frame page1


class Page1(tk.Frame):

    applyname = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background=backgroundColor)

        username = tk.Entry(self, bg=btncolor, highlightthickness=0, bd='0', fg='white', justify=CENTER,
                            highlightcolor='white')
        applyname = tk.Button(self, bg=btncolor, highlightthickness=0, bd='0', text="Apply", command=submit())
        nextpage = tk.Button(self, bg=btncolor, highlightthickness=0, bd='0', text="Next")
        welcome = tk.Label(self, text="Welcome to League simulator! Please type your name", font=LARGEFONT,
                           bg=backgroundColor, foreground='white')
        typenamehere = tk.Label(self, text="Type name here",
                                bg=backgroundColor, foreground='white')

        # Place Button,Text etc.
        welcome.place(relx=0.5, rely=0.1, anchor=CENTER)
        username.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.1, anchor=CENTER)
        applyname.place(relx=0.65, rely=0.5, relwidth=0.05, relheight=0.1, anchor=CENTER)
        typenamehere.place(relx=0.5, rely=0.4, anchor=CENTER)

    # third window frame page2


class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background=backgroundColor)

        username = tk.Entry(self, bg=btncolor, highlightthickness=0, bd='0', fg='white', justify=CENTER,
                            highlightcolor='white')
        applyname = tk.Button(self, bg=btncolor, highlightthickness=0, bd='0', text="Apply")
        welcome = tk.Label(self, text="Welcome to League simulator! Please type your name", font=LARGEFONT,
                           bg=backgroundColor, foreground='white')
        typenamehere = tk.Label(self, text="Type name here",
                                bg=backgroundColor, foreground='white')

        # Place Button,Text etc.
        welcome.place(relx=0.5, rely=0.1, anchor=CENTER)
        username.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.1, anchor=CENTER)
        applyname.place(relx=0.65, rely=0.5, relwidth=0.05, relheight=0.1, anchor=CENTER, command=submit)
        typenamehere.place(relx=0.5, rely=0.4, anchor=CENTER)

    # third window frame page2


root = tkinterApp()
root.mainloop()
