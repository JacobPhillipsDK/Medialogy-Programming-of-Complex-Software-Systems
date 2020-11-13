from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.scrolledtext as st
from main2 import *

SmallFont = ("Verdana", 20, "bold")
myFont = ("Helvetica", 50)

backgroundColor = '#350f58'
btncolor = '#884dbc'
TotalMoney = 100
newplayers = []


def close_window():
    root.destroy()

def PlaceImage(self):
    load = Image.open("BackgroundPic.png")
    render = ImageTk.PhotoImage(load)
    # labels can be text or images
    img = Label(self, image=render)
    img.image = render
    img.place(x=0, y=0)


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
        for F in (StartPage, Page1, Page2, Page3):
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
        start = tk.Button(self, bg=btncolor, font=myFont, highlightthickness=0, bd='0', text="START",
                          command=lambda: controller.show_frame(Page1))
        start.place(relx=0.5, rely=0.5, relwidth=0.40, relheight=0.20, anchor=CENTER)

    # second window frame page1


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background=backgroundColor)

        singeplayer = tk.Button(self, font=myFont, bg=btncolor, highlightthickness=0, bd='0',
                                text="Single-player",
                                command=lambda: controller.show_frame(Page2))
        multiplayer = tk.Button(self, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="MultiPlayer",
                                command=None)

        singeplayer.place(relx=0.5, rely=0.35, relwidth=0.40, relheight=0.20, anchor=CENTER)
        multiplayer.place(relx=0.5, rely=0.65, relwidth=0.40, relheight=0.20, anchor=CENTER)

    # third window frame page2

    # Single player page


class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background=backgroundColor)
        self.scrollbar = Scrollbar(self)
        PlaceImage(self)
        self.listbox = tk.Listbox(self)
        # Creating Labels,Entry,Button
        self.PlayerCost = Label(self, font=SmallFont, text="Cost", bg=backgroundColor, foreground='white')
        self.SearchCost_Text = Label(self, font=SmallFont, text="Type to search after cost", bg=backgroundColor,
                                     foreground='white')
        self.buy_btn = tk.Button(self, font=SmallFont, bg=btncolor, highlightthickness=0, bd='0', text="BUY",
                                 command=self.BuyMenu)
        self.Search_cost = tk.Entry(self, bg=btncolor, font=SmallFont, foreground='white')
        self.Money = Label(self, font=myFont, text=TotalMoney, bg=backgroundColor, foreground='white')
        self.Money.place(relx=0.1, rely=0.1, anchor=CENTER)

        # Placing the Labels,Entry,Button
        self.PlayerCost.place(relx=0.895, rely=0.1, anchor=CENTER)
        self.SearchCost_Text.place(relx=0.4, rely=0.35, anchor=CENTER)
        self.Search_cost.place(relx=0.4, rely=0.475, relwidth=0.2, relheight=0.1, anchor=CENTER)
        self.buy_btn.place(relx=0.8, rely=0.9, relwidth=0.1, relheight=0.1, anchor=CENTER)
        self.startGame = tk.Button(self, font=SmallFont, bg=btncolor, highlightthickness=0, bd='0', text="Start Game",
                                   command=lambda: controller.show_frame(Page3))

        self.listbox.place(relx=0.8, rely=0.55, relheight=0.50, anchor=CENTER)

        for i in range(len(allPlayers)):
            self.listbox.insert(i, allPlayers[i].getName() + "        cost:" + str(allPlayers[i].getCost()))
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def BuyMenu(self):
        global Pressed
        if len(newplayers) == 0:
            number = self.listbox.index(ANCHOR)
        else:
            Pressed += 1
            number = self.listbox.index(ANCHOR) + Pressed
        global TotalMoney
        if TotalMoney - allPlayers[number].getCost() >= 0:
            players1.append(allPlayers[number])
            TotalMoney -= allPlayers[number].getCost()
            self.Money.destroy()
            moneytext = Label(self, font=myFont, text=TotalMoney, bg=backgroundColor, foreground='white')
            moneytext.place(relx=0.1, rely=0.1, anchor=CENTER)
            self.listbox.delete(ANCHOR)
            print("total: ", TotalMoney)
            if len(players1) == 5:
                return self.startGame.place(relx=0.45, rely=0.85, relwidth=0.2, relheight=0.1,
                                            anchor=CENTER), self.buy_btn.place_forget()
        else:
            failtekst = Label(self, font=SmallFont, text="You don't have enough money!", bg=backgroundColor,
                              foreground="white")
            failtekst.place(relx=0.3, rely=0.1, anchor=CENTER)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background=backgroundColor)
        self.text_area = st.ScrolledText(self, width=52, height=20, font=SmallFont, bg=backgroundColor,
                                         foreground='white', relief=GROOVE, bd=0)
        self.closeBtn = tk.Button(self, font=SmallFont, bg=btncolor, highlightthickness=0, bd='0', text="Exit",
                                command=close_window)

        print("Results page")
        open("output.txt", "w").close()
        GameResults = readFile("output.txt")
        startGame()
        self.text_area.place(relx=0.275, rely=0.5, anchor=CENTER)
        self.text_area.insert(tk.INSERT, applytoLabel(GameResults))
        self.text_area.configure(state='disabled')
        self.closeBtn.place(relx=0.8, rely=0.3, relwidth=0.3, relheight=0.1, anchor=CENTER)
        print(GameResults)


root = tkinterApp()
root.mainloop()
