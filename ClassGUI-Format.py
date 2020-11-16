from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.scrolledtext as st
from main2 import *
from gameSimulator import *
from Team import *

SmallFont = ("Verdana", 20, "bold")
myFont = ("Helvetica", 50)

backgroundColor = '#320041'
btncolor = '#884dbc'

TotalMoney = 100
newplayers = []
searchedPlayers = []



def close_window():
    root.destroy()


def PlaceImage(self):
    load = Image.open("Assets/BackgroundPic.png")
    render = ImageTk.PhotoImage(load)
    # labels can be text or images
    img = Label(self, image=render)
    img.image = render
    img.place(x=0, y=0)


def PlaceImage2(self):
    load = Image.open("Assets/Background2.jpg")
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
        self.iconbitmap("Assets/poro-icon.ico")
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
        PlaceImage2(self)
        self.start = tk.Button(self, bg=btncolor, font=myFont, highlightthickness=0, bd='0', text="START",
                               command=lambda: controller.show_frame(Page1))
        self.start.place(relx=0.5, rely=0.5, relwidth=0.40, relheight=0.20, anchor=CENTER)

    # second window frame page1


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background=backgroundColor)
        PlaceImage2(self)
        self.singeplayer = tk.Button(self, font=myFont, bg=btncolor, highlightthickness=0, bd='0',
                                     text="Single-player",
                                     command=lambda: controller.show_frame(Page2))
        self.smultiplayer = tk.Button(self, font=myFont, bg=btncolor, highlightthickness=0, bd='0', text="MultiPlayer",
                                      command=None)

        self.singeplayer.place(relx=0.5, rely=0.35, relwidth=0.40, relheight=0.20, anchor=CENTER)
        self.smultiplayer.place(relx=0.5, rely=0.65, relwidth=0.40, relheight=0.20, anchor=CENTER)
        players1.clear()
    # third window frame page2

    # Single player page


class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background=backgroundColor)
        PlaceImage(self)

        # Scrollbar and Listbox
        self.scrollbar = Scrollbar(self)
        self.listbox = tk.Listbox(self)
        self.listboxsearch = tk.Listbox(self)

        # Labels
        self.Total_money = Label(self, font=SmallFont, text="Total gold:", bg=backgroundColor, foreground='white')
        self.PlayerCost = Label(self, font=SmallFont, text="Cost", bg=backgroundColor,foreground='white')
        self.SearchCost_Text = Label(self, font=SmallFont, text="Type to search after cost", bg=backgroundColor,
                                    foreground='white')
        self.Money = Label(self, font=myFont, text=TotalMoney, bg=backgroundColor, foreground='white')
        self.sortByCost_btn = tk.Button(self, font=SmallFont, bg=btncolor, highlightthickness=0, bd='0',
                                        text="Sort After Cost", foreground='white', command=self.Sort)

        # Buttons
        self.buy_btn = tk.Button(self, font=SmallFont, bg=btncolor, highlightthickness=0, bd='0', text="BUY", foreground='white',
                                 command=self.BuyMenu)
        self.startGame = tk.Button(self, font=SmallFont, bg=btncolor, highlightthickness=0, bd='0', text="Start Game",
                                   command=lambda: controller.show_frame(Page3))
        self.searchByCost_btn = tk.Button(self, font=SmallFont, bg=btncolor, highlightthickness=0, bd='0',
                                          text="SEARCH", foreground = 'white',command=self.Search1)
        self.clear_btn = tk.Button(self, font=SmallFont, bg=btncolor, highlightthickness=0, bd='0', text="CLEAR SEARCH", foreground='white', command=self.clearSearch)

        # Entry
        self.Search_cost = tk.Entry(self, bg=btncolor, font=SmallFont, foreground='white')

        # Placing all
        self.Total_money.place(relx=0.10, rely=0.1, anchor=CENTER)
        self.Money.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.PlayerCost.place(relx=0.800, rely=0.1, anchor=CENTER)
        self.SearchCost_Text.place(relx=0.45, rely=0.35, anchor=CENTER)
        self.Search_cost.place(relx=0.45, rely=0.475, relwidth=0.2, relheight=0.1, anchor=CENTER)
        self.buy_btn.place(relx=0.8, rely=0.9, relwidth=0.1, relheight=0.1, anchor=CENTER)
        self.sortByCost_btn.place(relx=0.15, rely=0.85, relwidth=0.2, relheight=0.1, anchor=CENTER)
        self.listbox.place(relx=0.8, rely=0.55, relheight=0.50, relwidth=0.1, anchor=CENTER)
        self.searchByCost_btn.place(relx=0.45, rely=0.57, relwidth=0.1, relheight=0.05, anchor=CENTER)
        self.clear_btn.place(relx=0.15, rely=0.57, relwidth=0.2, relheight=0.05, anchor=CENTER)

        for i in range(len(allPlayers)):
            self.listbox.insert(i, allPlayers[i].getName() + "        cost:" + str(allPlayers[i].getCost()))
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        print(TotalMoney)
        players1.clear()

    def BuyMenu(self):
        number = self.listbox.index(ANCHOR)
        global TotalMoney
        if TotalMoney - allPlayers[number].getCost() >= 0:
            players1.append(allPlayers[number])
            TotalMoney -= allPlayers[number].getCost()
            self.Money.destroy()
            self.moneytext = Label(self, font=myFont, text=TotalMoney, bg=backgroundColor, foreground='white')
            self.moneytext.place(relx=0.5, rely=0.1, relwidth=0.2, anchor=CENTER)
            print("total: ", TotalMoney)
            if len(players1) == 5:
                return self.startGame.place(relx=0.45, rely=0.85, relwidth=0.2, relheight=0.1,
                                            anchor=CENTER), self.buy_btn.place_forget()
        else:

            self.failtekst = Label(self, font=SmallFont, text="You don't have enough money!", bg=backgroundColor,
                                   foreground="white")
            self.failtekst.place(relx=0.3, rely=0.1, anchor=CENTER)

    def Sort(self):
        self.listbox.delete(first=0, last=len(allPlayers))
        for i in range(len(allPlayers) - 1, 0, -1):
            for j in range(i):
                if allPlayers[j].getCost() > allPlayers[j + 1].getCost():
                    allPlayers[j], allPlayers[j + 1] = allPlayers[j + 1], allPlayers[j]
        self.listbox.place(relx=0.8, rely=0.55, relheight=0.50, relwidth=0.1, anchor=CENTER)
        for i in range(len(allPlayers)):
            self.listbox.insert(i, allPlayers[i].getName() + "        cost:" + str(allPlayers[i].getCost()))
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        return

    def Search1(self):
        self.listboxsearch.delete(first=0, last=len(allPlayers))
        value = int(self.Search_cost.get())
        for i in range(len(allPlayers)):
            if allPlayers[i].getCost() == value:
                searchedPlayers.append(allPlayers[i])
        for i in range(len(searchedPlayers)):
            self.listboxsearch.insert(i, searchedPlayers[i].getName() + "        cost:" + str(
                searchedPlayers[i].getCost()))
        self.listboxsearch.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.place_forget()
        self.listboxsearch.place(relx=0.8, rely=0.55, relheight=0.50, relwidth=0.1, anchor=CENTER)
        self.listboxsearch.delete(ANCHOR)
        # self.buy_btn2.place(relx=0.45, rely=0.85, relwidth=0.2, relheight=0.1, anchor=CENTER)
        # self.buy_btn.place_forget()
        return

    def Buysearch(self):
        self.listbox.delete(first=0, last=len(searchedPlayers))
        number = self.listboxsearch.index(ANCHOR)
        global TotalMoney
        if TotalMoney - searchedPlayers[number].getCost() >= 0:
            players1.append(searchedPlayers[number])
            TotalMoney -= searchedPlayers[number].getCost()
            self.moneytext = Label(self, font=SmallFont, text=TotalMoney, bg=backgroundColor, foreground='white')
            self.moneytext.place(relx=0.5, rely=0.1, anchor=CENTER)
            print("total: ", TotalMoney)
            if len(players1) == 5:
                self.moneytext.place_forget()
                self.sortByCost_btn.place_forget()
                return self.startGame.place(relx=0.45, rely=0.85, relwidth=0.2, relheight=0.1,
                                            anchor=CENTER), self.buy_btn.place_forget()
        else:
            self.failtekst = Label(self, font=SmallFont, text="You don't have enough money!", bg=backgroundColor,
                                   foreground="white")
            self.failtekst.place(relx=0.1, rely=0.1, anchor=CENTER)
        return

    def clearSearch(self):
        self.listbox.delete(first=0, last=len(allPlayers))
        self.listbox.place(relx=0.8, rely=0.55, relheight=0.50, relwidth=0.1, anchor=CENTER)
        for i in range(len(allPlayers)):
            self.listbox.insert(i, allPlayers[i].getName() + "        cost:" + str(allPlayers[i].getCost()))
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.listboxsearch.place_forget()
        searchedPlayers.clear()
        # self.buy_btn.place(relx=0.45, rely=0.85, relwidth=0.2, relheight=0.1, anchor=CENTER)
        self.buy_btn2.place_forget()
        return


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.update_idletasks()
        self.config(background=backgroundColor)
        # Button / Label
        self.text_area = st.ScrolledText(self, width=52, height=20, font=SmallFont, bg=backgroundColor,
                                         foreground='white', relief=GROOVE, bd=0)
        self.closeBtn = tk.Button(self, font=SmallFont, bg=btncolor, highlightthickness=0, bd='0', text="Exit",
                                  command=close_window)
        print("Results page")
        open("output.txt", "w").close()
        GameResults = readFile("output.txt")
        self.text_area.place(relx=0.275, rely=0.5, anchor=CENTER)
        self.text_area.insert(tk.INSERT, applytoLabel(GameResults))
        self.text_area.configure(state='disabled')
        startGame()
        GameResults = readFile("output.txt")
        self.closeBtn.place(relx=0.8, rely=0.3, relwidth=0.3, relheight=0.1, anchor=CENTER)
        print(GameResults)



root = tkinterApp()
root.mainloop()
