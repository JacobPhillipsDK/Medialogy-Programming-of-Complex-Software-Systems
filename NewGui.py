from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.scrolledtext as st
from main2 import *

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
moneyLeft = "MONEY :" + str(TotalMoney)


# Reads TXT file and saves it Into a List
def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words



def applytoLabel(input):
    n = len(input)
    element = ''
    for i in range(n):
        element = element + input[i] + '\n'
    return element


def startProgram(frame):
    frame()
    return None


def frame1():
    return StartPage()


def frame2():
    return SecondPage()


def frame3():
    return SinglePLayerPage()


def frame4():
    return NextSinglePlayerPage()


def notWorking():
    messagebox.showinfo("Under development", "This option does currently not work, please try Single-player mode")


canvas = tk.Canvas(root, width=1500, height=720, highlightthickness=0, borderwidth=0)
img = ImageTk.PhotoImage(Image.open("BackgroundPic.png"), Image.ANTIALIAS)
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
frame = Frame(root)

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
buy_btn = tk.Button(root, font=buy_btn, bg=btncolor, highlightthickness=0, bd='0', text="BUY",
                    command=frame4)

# Texts
MoneyText = Label(root, font=myFont2, text=moneyLeft, bg=backgroundColor, foreground='white')
PlayerName = Label(root, font=myFont2, text="Name", bg=backgroundColor, foreground='white')
PlayerCost = Label(root, font=myFont2, text="Cost", bg=backgroundColor, foreground='white')
SearchCost_Text = Label(root, font=SearchFont, text="Type to search after cost", bg=backgroundColor, foreground='white')

# Entry box
Search_name = tk.Entry(root, bg=btncolor, font=SearchFont, foreground='white')
Search_cost = tk.Entry(root, bg=btncolor, font=SearchFont, foreground='white')


# Background


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
    canvas.pack()
    frame.pack()
    MoneyText.place(relx=0.1, rely=0.1, anchor=CENTER)
    PlayerCost.place(relx=0.895, rely=0.1, anchor=CENTER)
    SearchCost_Text.place(relx=0.4, rely=0.35, anchor=CENTER)
    Search_cost.place(relx=0.4, rely=0.475, relwidth=0.2, relheight=0.1, anchor=CENTER)
    buy_btn.place(relx=0.45, rely=0.85, relwidth=0.2, relheight=0.1, anchor=CENTER)
    startGame()


def NextSinglePlayerPage():
    open("output.txt", "w").close()
    canvas.destroy()
    frame.destroy()
    MoneyText.destroy()
    PlayerCost.destroy()
    SearchCost_Text.destroy()
    Search_cost.destroy()
    buy_btn.destroy()
    GameResults = readFile("output.txt")
    text_area = st.ScrolledText(root, width=50, height=10, font=myFont2, bg=backgroundColor,foreground='white')
    text_area.place(relx=0.5, rely=0.4, anchor=CENTER)
    text_area.insert(tk.INSERT, applytoLabel(GameResults))
    text_area.configure(state='disabled')


def close_window():
    root.destroy()


# Remeber to change this to the StartPage
startProgram(frame1)
root.mainloop()
