import socket
from tkinter import *
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
import tkinter.scrolledtext as st
from main2 import *
import os

# Networking Stuff:
HEADER = 64
PORT = 5060
HEADERSIZE = 64
# Hvilken formatering som programmet vil blive kørt i
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

root = Tk()
root.title("Sim League")
root.geometry("1500x720")
root.iconbitmap("Assets/poro-icon.ico")
backgroundColor = '#350f58'
btncolor = '#884dbc'
textColor = '#31013F'
root.config(background=backgroundColor)
root.resizable(width=False, height=False)

backgroundImage = ImageTk.PhotoImage(
    file="Assets/Shape 3.png")

global Clicked
Clicked = 0
global TotalMoney
TotalMoney = 100
newplayers = []
searchedPlayers = []


def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# Reads TXT file and saves it Into a List
def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words


# Gemmer data til DataGem
def GemSata(InputData):
    file2Write = open("Filer der ikke bliver brugt mere/DataGem.txt", "a")
    file2Write.write(f"{InputData}")
    file2Write.close()
    return None


# Læser linjer fra TXT fil
def ReadLinesTxt():
    SavedLines = send_msg()
    InputData = open("Filer der ikke bliver brugt mere/DataGem.txt", "r")
    for line in InputData:
        # Should print each line of
        # print(line)
        SavedLines.append(line[:-1])
    InputData.close()
    return SavedLines

def resetMoney():
    global TotalMoney
    TotalMoney = 100
    players1.clear()


def applytoLabel(SetInput):
    n = len(SetInput)
    element = ''
    for i in range(n):
        element = element + SetInput[i] + '\n'
    return element


def readStringExecutive(String):
    a = str(String)
    # Was used for debugging purposes
    # print(a)
    exec(a)


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
        if Clicked == True:
            send_msg(f"players3.append(allPlayers[{number}])")
        # GemSata(f"players1.append(allPlayers[{number}]\n")
        print(f"Wrote Number: {number} to file")
        TotalMoney -= allPlayers[number].getCost()
        moneytext = Label(root, font=myFont2, text=TotalMoney, bg=textColor, foreground='white')
        moneytext.place(relx=0.3, rely=0.1,relwidth=0.2, anchor=CENTER)
        if len(players1) == 5:
            moneytext.place_forget()
            sortByCost_btn.place_forget()
            if Clicked == 1:
                return MultiPlayerResult()
            else:
                return NextSinglePlayerPage()
    else:
        failtekst = Label(root, font=myFont2, text="You don't have enough money!", bg=textColor,
                          foreground="white")
        failtekst.place(relx=0.3, rely=0.3, anchor=CENTER)


def multiplayer_frame():
    frame2_btn1.place_forget()
    frame2_btn2.place_forget()
    global Clicked
    Clicked += 1
    print(Clicked)
    return multiplayer_connect(),


def MultiPlayerResult():
    return NextMultiplayerPage()


def Sort():
    listbox.delete(first=0, last=len(allPlayers))
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
    listboxsearch.delete(first=0, last=len(allPlayers))
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
    listbox.delete(first=0, last=len(searchedPlayers))
    number = listboxsearch.index(ANCHOR)
    global TotalMoney
    if TotalMoney - searchedPlayers[number].getCost() >= 0:
        players1.append(searchedPlayers[number])
        if Clicked == True:
            send_msg(f"players3.append(allPlayers[{number}])")
        GemSata(f"players3.append(allPlayers[{number}]\n")
        print(f"Wrote Number: {number} to file")
        TotalMoney -= searchedPlayers[number].getCost()
        moneytext = Label(root, font=myFont2, text=TotalMoney, bg=textColor, foreground='white')
        moneytext.place(relx=0.3, rely=0.1, relwidth=0.2, anchor=CENTER)
        print("total: ", TotalMoney)
        if len(players1) == 5:
            ReadLinesTxt()
            send_msg(ReadLinesTxt().encode(FORMAT))
            moneytext.place_forget()
            sortByCost_btn.place_forget()
            if Clicked == 1:
                return NextMultiplayerPage()
            else:
                return NextSinglePlayerPage()
    else:
        failtekst = Label(root, font=myFont2, text="You don't have enough money!", bg=backgroundColor,
                          foreground="white")
        failtekst.place(relx=0.1, rely=0.1, anchor=CENTER)
    return


def clearSearch():
    listbox.delete(first=0, last=len(allPlayers))
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


def close_window():
    root.destroy()

canvas = tk.Canvas(root, width=1500, height=720, highlightthickness=0, borderwidth=0)
img = ImageTk.PhotoImage(Image.open("Assets/BackgroundPic.png"), Image.ANTIALIAS)
canvas2 = tk.Canvas(root,width=1500, height=720, highlightthickness=0, borderwidth=0)
img2 =ImageTk.PhotoImage(Image.open("Assets/Background2.jpg"), Image.ANTIALIAS)
img = ImageTk.PhotoImage(Image.open("Assets/BackgroundPic.png"))
canvas2.background = img2
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
bg2 = canvas2.create_image(0,0, anchor =tk.NW, image = img2)
frame = Frame(root)


myFont = font.Font(family='Helvetica', size=50, weight='bold')
myFont2 = font.Font(family='Helvetica', size=30, weight='bold')
myFont3 = font.Font(family='Helvetica', size=20, weight='bold')
SearchFont = font.Font(family='Helvetica', size=20, weight='bold')
buy_btn = font.Font(family='Helvetica', size=30, weight='bold')
# Buttons
frame1_btn1 = frame1_btn1 = tk.Button(root, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="START", command=frame2, foreground='white')
frame2_btn1 = tk.Button(root, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="Single-player",foreground='white',
                        command=frame3)
frame2_btn2 = tk.Button(root, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="MultiPlayer",foreground='white',
                        command=multiplayer_frame)
buy_btn = tk.Button(root, font=buy_btn, bg=btncolor, highlightthickness=0, bd='0', text="BUY",foreground='white',
                    command=frame4)
buy_btn2 = tk.Button(root, font=myFont2, bg=btncolor, highlightthickness=0, bd='0', text="BUY",foreground='white',
                     command=Buysearch)
uy_btn3 = tk.Button(root, font=myFont3, bg=btncolor, highlightthickness=0, bd='0', text="BUY",foreground='white',
                    command=frame4)
exit_btn = tk.Button(root, font=myFont2, bg=btncolor, highlightthickness=0, bd='0', text="EXIT",foreground='white',
                     command=close_window)
sortByCost_btn = tk.Button(root, font=myFont2, bg=btncolor, highlightthickness=0, bd='0', text="SORT",foreground='white',
                    command=Sort)
searchByCost_btn = tk.Button(root, font=buy_btn, bg=btncolor, highlightthickness=0, bd='0', text="SEARCH",foreground='white',
                    command=Search1)
clear_btn = tk.Button(root, font=buy_btn, bg=btncolor, highlightthickness=0, bd='0', text="CLEAR SEARCH",foreground='white',
                    command=clearSearch)
reset_btn = tk.Button(root, font=buy_btn, bg=btncolor, highlightthickness=0, bd='0', text="BUY",
                    command=resetMoney())

# Texts
MoneyText = Label(root, font=myFont3, text=TotalMoney, bg=textColor, foreground='white')
PlayerName = Label(root, font=myFont2, text="Name", bg=textColor, foreground='white')
PlayerCost = Label(root, font=myFont2, text="Cost", bg=textColor, foreground='white')
SearchCost_Text = Label(root, font=SearchFont, text="Type to search after cost", bg=textColor, foreground='white')
text_area = st.ScrolledText(root, width=52, height=20, font=SearchFont, bg=textColor,
                            foreground='white', relief=GROOVE, bd=0)
TotalmoneyText = Label(root, font=myFont2, text="Total money:", bg=textColor, foreground='white')

# Entry box
Search_name = tk.Entry(root, bg=btncolor, font=SearchFont, foreground='white')
Search_cost = tk.Entry(root, bg=btncolor, font=SearchFont, foreground='white')
listbox = tk.Listbox(root)
listboxsearch = tk.Listbox(root)
scrollbar = Scrollbar(root)


# Background


def StartPage():
    print("StartPage")
    canvas2.pack()
    frame1_btn1.place(relx=0.5, rely=0.5, relwidth=0.40, relheight=0.20, anchor=CENTER)


def SecondPage():
    print("Second Page")
    canvas2.pack()
    frame1_btn1.place_forget()
    frame2_btn1.place(relx=0.5, rely=0.35, relwidth=0.40, relheight=0.20, anchor=CENTER)
    frame2_btn2.place(relx=0.5, rely=0.65, relwidth=0.40, relheight=0.20, anchor=CENTER)
    open("output.txt", "w").close()


def SinglePLayerPage():
    open("output.txt", "w").close()
    print("ThirdPage")
    frame2_btn1.place_forget()
    frame2_btn2.place_forget()
    canvas2.forget()
    canvas.pack()
    frame.pack()
    MoneyText.place(relx=0.3, rely=0.1, anchor=CENTER)
    TotalmoneyText.place(relx=0.1, rely=0.1, anchor=CENTER)
    PlayerCost.place(relx=0.800, rely=0.1, anchor=CENTER)
    SearchCost_Text.place(relx=0.3, rely=0.39, anchor=CENTER)
    Search_cost.place(relx=0.3, rely=0.475, relwidth=0.2, relheight=0.1, anchor=CENTER)
    buy_btn.place(relx=0.45, rely=0.85, relwidth=0.2, relheight=0.1, anchor=CENTER)
    sortByCost_btn.place(relx=0.15, rely=0.85, relwidth=0.2, relheight=0.1, anchor=CENTER)
    searchByCost_btn.place(relx=0.35, rely=0.57, relwidth=0.09, relheight=0.05, anchor=CENTER)
    clear_btn.place(relx=0.25, rely=0.57, relwidth=0.09, relheight=0.05, anchor=CENTER)
    reset_btn.place(relx=0.15, rely=0.57, relwidth=0.09, relheight=0.05, anchor=CENTER)
    # scrollbar.place(relx=0.4, rely=0.3, anchor=CENTER)
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
    TotalmoneyText.place_forget()
    clear_btn.place_forget()
    exit_btn.place(relx=0.8, rely=0.3, relwidth=0.6, relheight=0.1, anchor=CENTER)



def NextMultiplayerPage():
    canvas.forget()
    frame.place_forget()
    MoneyText.place_forget()
    listbox.place_forget()
    PlayerCost.place_forget()
    searchByCost_btn.place_forget()
    SearchCost_Text.place_forget()
    Search_cost.place_forget()
    TotalmoneyText.place_forget()
    clear_btn.place_forget()
    buy_btn.place_forget()
    GameResults = "Look at console for results"
    f = Label(root, font=myFont2, text=GameResults, bg=backgroundColor, foreground='white')
    f.place(relx=0.5, rely=0.1, relwidth=10, relheight=0.2, anchor=CENTER)
    exit_btn.place(relx=0.5, rely=0.4, relwidth=0.3, relheight=0.1, anchor=CENTER)


def multiplayer_connect():
    client.connect(ADDR)
    # send_msg("[USER] A user have connected to server")
    frame3()
    print(Clicked)


startProgram(frame1)
root.mainloop()
