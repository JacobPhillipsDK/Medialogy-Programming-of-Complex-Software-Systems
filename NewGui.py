from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

btn_width = 20
btn_height = 20

root = Tk()
root.title("Sim League")
root.geometry("1500x720")
root.iconbitmap("poro-icon.ico")
root.config(background='#350f58')
root.resizable(width=False, height=False)
btncolor = '#884dbc'

# creates a canvas for the application






def frame1():
    return StartPage()


def frame2():
    return SecondPage()


def frame3():
    return SinglePLayerPage()


def notWorking():
    messagebox.showinfo("Under development", "This option does currently not work, please try Single-player mode")


myFont = font.Font(family='Helvetica', size=50, weight='bold')
text = Label(root, font=myFont, text="Pane Title")
frame1_btn1 = tk.Button(root, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="START", command=frame2)
frame2_btn1 = tk.Button(root, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="Single-player",
                        command=frame3)
frame2_btn2 = tk.Button(root, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="MultiPlayer",
                        command=notWorking)


def StartPage():
    print("StartPage")
    frame1_btn1.place(relx=0.30, rely=0.42, relwidth=0.40, relheight=0.20)


def SecondPage():
    print("Second Page")
    frame1_btn1.destroy()
    text.place(relx=0.30, rely=0.25)
    frame2_btn1.place(relx=0.30, rely=0.25, relwidth=0.40, relheight=0.20)
    frame2_btn2.place(relx=0.30, rely=0.5, relwidth=0.40, relheight=0.20)


def SinglePLayerPage():
    print("ThirdPage")
    frame2_btn1.destroy()
    frame2_btn2.destroy()



def close_window():
    root.destroy()


# Remeber to change this to the StartPage
SinglePLayerPage()
root.mainloop()
