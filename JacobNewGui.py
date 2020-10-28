from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

backgroundColor = '#350f58'


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Sim League")
        master.geometry("1500x720")
        master.iconbitmap("poro-icon.ico")
        master.config(background=backgroundColor)
        master.resizable(width=False, height=False)
        master.title("A simple GUI")






root = Tk()
my_gui = GUI(root)
root.mainloop()
