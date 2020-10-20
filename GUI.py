import tkinter as tk

HEIGHT = 720
WIDTH = 1500
#Creates a window for the application.
Main_window = tk.Tk()
window = 0
Main_window.title("League simulator")


def window1():
    print("test1")
    newWindow()
    print(window)

def window2():
    teamWindow()
    print(window2)

def close_window():
    Main_window.destroy()

#creates a canvas for the application
canvas = tk.Canvas(Main_window, height = HEIGHT, width = WIDTH,)
#packs in the canvas
canvas.pack()

if window == 0:
    # creating a start button and inputs a text.
    Startbutton = tk.Button(Main_window, font=60, text="start", bg='grey', command = window1)
    Startbutton.place(relx=0.35, rely=0.4, relwidth=0.25, relheight=0.15)

def newWindow():
    print("test2")
    singlePlayer = tk.Button(Main_window, font=60, text ="Singleplayer", bg ='grey', command = window2)
    singlePlayer.place(relx=0.35, rely=0.2, relwidth=0.25, relheight =0.15)
    multiPlayer = tk.Button(Main_window, font=60, text="Multiplayer", bg='grey', command = window2)
    multiPlayer.place(relx=0.35, rely=0.4, relwidth=0.25, relheight=0.15)

def teamWindow():
     getTeam = tk.Button(Main_window, font = 60,text = "Get teams", bg ='grey', command = close_window)
     getTeam.place(relx=0.35, rely=0.2, relwidth=0.25, relheight =0.15)

#makes the program loop the main thread until exited
Main_window.mainloop()






