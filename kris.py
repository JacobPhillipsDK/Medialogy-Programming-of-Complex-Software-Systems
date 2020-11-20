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
root.iconbitmap("Assets/poro-icon.ico")
backgroundColor = '#350f58'
btncolor = '#884dbc'
root.config(background=backgroundColor)
root.resizable(width=False, height=False)

backgroundImage = ImageTk.PhotoImage(file="Assets/Shape 3.png")


global TotalMoney
TotalMoney = 100
newplayers = []
searchedPlayers = []


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
    players1.clear()
    return SinglePLayerPage()


def frame4():
    number = listbox.index(ANCHOR)
    global TotalMoney
    if TotalMoney - allPlayers[number].getCost() >= 0:
        players1.append(allPlayers[number])
        print(players1)
        TotalMoney -= allPlayers[number].getCost()
        moneytext = Label(root, font=myFont2, text=TotalMoney, bg=backgroundColor, foreground='white')
        moneytext.place(relx=0.1, rely=0.1, anchor=CENTER)
        if len(players1) == 5:
            sortByCost_btn.place_forget()
            moneytext.place_forget()
            return NextSinglePlayerPage()
    else:
        failtekst = Label(root, font=myFont2, text="You don't have enough money!",bg=backgroundColor,foreground="white")
        failtekst.place(relx=0.1,rely=0.1,anchor=CENTER)

def Sort():
    listbox.delete(first=0,last=len(allPlayers))
    for i in range(len(allPlayers) - 1, 0, -1):
        for j in range(i):
            if allPlayers[j].getCost() > allPlayers[j + 1].getCost():
                allPlayers[j], allPlayers[j + 1] = allPlayers[j + 1], allPlayers[j]
    listbox.place(relx=0.8, rely=0.55, relheight=0.50, anchor=CENTER)
    for i in range(len(allPlayers)):
        listbox.insert(i, allPlayers[i].getName() + "        cost:" + str(allPlayers[i].getCost()))
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    return

def Search1():
    listboxsearch.delete(first=0,last=len(allPlayers))
    value = int(Search_cost.get())
    for i in range(len(allPlayers)):
        if allPlayers[i].getCost() == value:
            searchedPlayers.append(allPlayers[i])
    for i in range(len(searchedPlayers)):
        listboxsearch.insert(i, searchedPlayers[i].getName() + "        cost:" + str(searchedPlayers[i].getCost()))
    listboxsearch.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.place_forget()
    listboxsearch.place(relx=0.8, rely=0.55, relheight=0.50, anchor=CENTER)
    buy_btn2.place(relx=0.45, rely=0.85, relwidth=0.2, relheight=0.1, anchor=CENTER)
    buy_btn.place_forget()
    return

def Buysearch():
    listbox.delete(first=0,last=len(searchedPlayers))
    number = listboxsearch.index(ANCHOR)
    global TotalMoney
    if TotalMoney - searchedPlayers[number].getCost() >= 0:
        players1.append(searchedPlayers[number])
        TotalMoney -= searchedPlayers[number].getCost()
        moneytext = Label(root, font=myFont2, text=TotalMoney, bg=backgroundColor, foreground='white')
        moneytext.place(relx=0.1, rely=0.1, anchor=CENTER)
        print("total: ", TotalMoney)
        if len(players1) == 5:
            moneytext.place_forget()
            sortByCost_btn.place_forget()
            return NextSinglePlayerPage()
    else:
        failtekst = Label(root, font=myFont2, text="You don't have enough money!", bg=backgroundColor,
                          foreground="white")
        failtekst.place(relx=0.1, rely=0.1, anchor=CENTER)
    return

def clearSearch():
    listbox.delete(first=0,last=len(allPlayers))
    listbox.place(relx=0.8, rely=0.55, relheight=0.50, anchor=CENTER)
    for i in range(len(allPlayers)):
        listbox.insert(i, allPlayers[i].getName() + "        cost:" + str(allPlayers[i].getCost()))
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listboxsearch.place_forget()
    searchedPlayers.clear()
    buy_btn.place(relx=0.45, rely=0.85, relwidth=0.2, relheight=0.1, anchor=CENTER)
    buy_btn2.place_forget()
    return


def reStart():
    return restartGame()


def notWorking():
    messagebox.showinfo("Under development", "This option does currently not work, please try Single-player mode")


canvas = tk.Canvas(root, width=1500, height=720, highlightthickness=0, borderwidth=0)
img = ImageTk.PhotoImage(Image.open("Assets/BackgroundPic.png"), Image.ANTIALIAS)
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
frame = Frame(root)

myFont = font.Font(family='Helvetica', size=50, weight='bold')
myFont2 = font.Font(family='Helvetica', size=30, weight='bold')
myFont3 = font.Font(family='Helvetica', size=20, weight='bold')
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
buy_btn2 = tk.Button(root, font=myFont2, bg=btncolor, highlightthickness=0, bd='0', text="BUY",
                    command=Buysearch)
buy_btn3 = tk.Button(root, font=myFont3, bg=btncolor, highlightthickness=0, bd='0', text="BUY",
                    command=frame4)
Restart_btn = tk.Button(root, font=myFont2, bg=btncolor, highlightthickness=0, bd='0', text="RESTART",
                        command=reStart)
sortByCost_btn = tk.Button(root, font=myFont2, bg=btncolor, highlightthickness=0, bd='0', text="SORT",
                    command=Sort)
searchByCost_btn = tk.Button(root, font=buy_btn, bg=btncolor, highlightthickness=0, bd='0', text="SEARCH",
                    command=Search1)
clear_btn = tk.Button(root, font=buy_btn, bg=btncolor, highlightthickness=0, bd='0', text="CLEAR SEARCH",
                    command=clearSearch)


# Texts
MoneyText = Label(root, font=myFont3, text=TotalMoney, bg=backgroundColor, foreground='white')
PlayerName = Label(root, font=myFont2, text="Name", bg=backgroundColor, foreground='white')
PlayerCost = Label(root, font=myFont2, text="Cost", bg=backgroundColor, foreground='white')
SearchCost_Text = Label(root, font=SearchFont, text="Type to search after cost", bg=backgroundColor, foreground='white')
text_area = st.ScrolledText(root, width=52, height=20, font=SearchFont, bg=backgroundColor,
                            foreground='white', relief=GROOVE, bd=0)
root.update_idletasks()

# Entry box
Search_name = tk.Entry(root, bg=btncolor, font=SearchFont, foreground='white')
Search_cost = tk.Entry(root, bg=btncolor, font=SearchFont, foreground='white')
listbox = tk.Listbox(root)
listboxsearch = tk.Listbox(root)
scrollbar = Scrollbar(root)



# Background


def StartPage():
    print("StartPage")
    frame1_btn1.place(relx=0.5, rely=0.5, relwidth=0.40, relheight=0.20, anchor=CENTER)


def SecondPage():
    print("Second Page")
    frame1_btn1.place_forget()
    frame2_btn1.place(relx=0.5, rely=0.35, relwidth=0.40, relheight=0.20, anchor=CENTER)
    frame2_btn2.place(relx=0.5, rely=0.65, relwidth=0.40, relheight=0.20, anchor=CENTER)
    open("output.txt", "w").close()


def SinglePLayerPage():
    print("ThirdPage")
    frame2_btn1.place_forget()
    frame2_btn2.place_forget()
    canvas.pack()
    frame.pack()
    MoneyText.place(relx=0.1, rely=0.1, anchor=CENTER)
    PlayerCost.place(relx=0.895, rely=0.1, anchor=CENTER)
    SearchCost_Text.place(relx=0.4, rely=0.39, anchor=CENTER)
    Search_cost.place(relx=0.4, rely=0.475, relwidth=0.2, relheight=0.1, anchor=CENTER)
    buy_btn.place(relx=0.45, rely=0.85, relwidth=0.2, relheight=0.1, anchor=CENTER)
    sortByCost_btn.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1,anchor=CENTER)
    searchByCost_btn.place(relx=0.45,rely=0.57,relwidth=0.09,relheight=0.05,anchor=CENTER)
    clear_btn.place(relx=0.35,rely=0.57,relwidth=0.09,relheight=0.05,anchor=CENTER)

    #scrollbar.place(relx=0.4, rely=0.3, anchor=CENTER)
    listbox.place(relx=0.8, rely=0.55, relheight=0.50, anchor=CENTER)


    for i in range(len(allPlayers)):
        listbox.insert(i, allPlayers[i].getName() + "        cost:" + str(allPlayers[i].getCost()))
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

def NextSinglePlayerPage():
    print("Results page")
    open("output.txt", "w").close()
    startGame()
    canvas.forget()
    frame.place_forget()
    MoneyText.place_forget()
    listbox.place_forget()
    PlayerCost.place_forget()
    SearchCost_Text.place_forget()
    Search_cost.place_forget()
    buy_btn.place_forget()
    GameResults = readFile("output.txt")
    text_area.place(relx=0.275, rely=0.5, anchor=CENTER)
    text_area.insert(tk.INSERT, applytoLabel(GameResults))
    text_area.configure(state='disabled')
    Restart_btn.place(relx=0.8, rely=0.3, relwidth=0.3, relheight=0.1, anchor=CENTER)
    print(GameResults)


def restartGame():
    Restart_btn.place_forget()
    text_area.place_forget()
    text_area.frame.place_forget()
    startProgram(frame2)
    global TotalMoney
    TotalMoney = 100
    players1.clear()


def close_window():
    root.destroy()


# Remeber to change this to the StartPage
startProgram(frame1)
root.mainloop()
