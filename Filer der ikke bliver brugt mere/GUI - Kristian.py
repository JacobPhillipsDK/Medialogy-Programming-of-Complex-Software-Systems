import tkinter as tk
from tkinter import filedialog,Text
import os

frontscreen = tk.Tk()

labelWelcome = tk.Label(frontscreen,text="Welcome to LoL manager!",padx=100,pady=10,font=(None,30),fg = "red")
labelWelcome.pack()
labelName = tk.Label(frontscreen,text="Enter your desired name")
labelName.pack()
name = tk.Entry(frontscreen)
name.pack()
name.get()
beginGame = tk.Button(frontscreen, text="Begin Game",padx=20,pady=10,fg="black",bg="black")
beginGame.pack()

frontscreen.mainloop()