from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

from PIL import ImageTk

root = Tk()
root.title("Sim League")
root.geometry("1500x720")
root.iconbitmap("poro-icon.ico")
backgroundColor = '#350f58'
root.config(background=backgroundColor)
root.resizable(width=False, height=False)
btncolor = '#884dbc'

backgroundImage = ImageTk.PhotoImage(file="Shape 3.png")

TotalMoney = 100
moneyLeft = "Money :" + str(TotalMoney)


# creates a canvas for the application
def startProgram(frame):
    frame()
    return None


def frame1():
    return StartPage()


def frame2():
    return SecondPage()


def frame3():
    return SinglePLayerPage()


def notWorking():
    messagebox.showinfo("Under development", "This option does currently not work, please try Single-player mode")


myFont = font.Font(family='Helvetica', size=50, weight='bold')
myFont2 = font.Font(family='Helvetica', size=30, weight='bold')
SearchFont = font.Font(family='Helvetica', size=20, weight='bold')
buy_btn = font.Font(family='Helvetica', size=30, weight='bold')
# Buttons
frame1_btn1 = tk.Button(root, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="START", command=frame2)
frame2_btn1 = tk.Button(root, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="Single-player",
                        command=frame3)
frame2_btn2 = tk.Button(root, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="MultiPlayer",
                        command=notWorking)
buy_btn = tk.Button(root, font=buy_btn, bg=btncolor, highlightthickness=0, bd='0', text="buy",
                    command=SearchFont)

# Texts
MoneyText = Label(root, font=myFont2, text=moneyLeft, bg=backgroundColor, foreground='white')
PlayerName = Label(root, font=myFont2, text="Name", bg=backgroundColor, foreground='white')
PlayerCost = Label(root, font=myFont2, text="Cost", bg=backgroundColor, foreground='white')
SearchBox_Text = Label(root, font=SearchFont, text="Type to search after name", bg=backgroundColor, foreground='white')
SearchCost_Text = Label(root, font=SearchFont, text="Type to search after cost", bg=backgroundColor, foreground='white')

# Entry box
Search_name = tk.Entry(root, bg=btncolor, font=SearchFont, foreground='white')
Search_cost = tk.Entry(root, bg=btncolor, font=SearchFont, foreground='white')

# Background
background_label = Label(root, image=backgroundImage)


def StartPage():
    print("StartPage")
    frame1_btn1.place(relx=0.5, rely=0.5, relwidth=0.40, relheight=0.20, anchor=CENTER)


def SecondPage():
    print("Second Page")
    frame1_btn1.destroy()
    frame2_btn1.place(relx=0.5, rely=0.35, relwidth=0.40, relheight=0.20, anchor=CENTER)
    frame2_btn2.place(relx=0.5, rely=0.65, relwidth=0.40, relheight=0.20, anchor=CENTER)


def SinglePLayerPage():
    print("ThirdPage")
    frame2_btn1.destroy()
    frame2_btn2.destroy()
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    MoneyText.place(relx=0.1, rely=0.1, anchor=CENTER)
    PlayerName.place(relx=0.795, rely=0.1, anchor=CENTER)
    PlayerCost.place(relx=0.895, rely=0.1, anchor=CENTER)
    SearchBox_Text.place(relx=0.15, rely=0.3, anchor=CENTER)
    SearchCost_Text.place(relx=0.4, rely=0.3, anchor=CENTER)
    Search_name.place(relx=0.15, rely=0.4, relwidth=0.2, relheight=0.1, anchor=CENTER)
    Search_cost.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1, anchor=CENTER)
    buy_btn.place(relx=0.5, rely=0.65, relwidth=0.2, relheight=0.1, anchor=CENTER)


def close_window():
    root.destroy()


# Remeber to change this to the StartPage
startProgram(SinglePLayerPage)
root.mainloop()
