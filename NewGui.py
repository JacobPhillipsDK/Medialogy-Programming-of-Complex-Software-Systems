import tkinter as tk

HEIGHT = 720
WIDTH = 1500
# Creates a window for the application.
Main_window = tk.Tk()
window = 1
Main_window.title("League of Legends - Simulator")


def vindueSkifter():
    print("test1")
    # selectWindow()
    getWindow()
    # matchWindow()
    print(window)


btncolor = '#884dbc'


def close_window():
    Main_window.destroy()


# creates a canvas for the application
canvas = tk.Canvas(Main_window, height=HEIGHT, width=WIDTH, bg='#350f58', highlightthickness=0)
# packs in the canvas
canvas.pack()

moveBtn = 0.2

# background image for the startup.
# background_image = tk.PhotoImage(file='startImage.jpeg')
background_label = tk.Label(Main_window)

if window == 1:
    # creating a start button and inputs a text.
    Startbutton = tk.Button(Main_window, font=60, text="start", bg='grey', command=vindueSkifter)
    btn1 = tk.Button(Main_window, font=100, bg=btncolor, highlightthickness=0, bd='0', text="Top")
    btn2 = tk.Button(Main_window, font=100, bg=btncolor, highlightthickness=0, bd='0', text="Jungle")
    btn3 = tk.Button(Main_window, font=100, bg=btncolor, highlightthickness=0, bd='0', text="Mid")
    btn4 = tk.Button(Main_window, font=100, bg=btncolor, highlightthickness=0, bd='0', text="ADC")
    btn5 = tk.Button(Main_window, font=100, bg=btncolor, highlightthickness=0, bd='0', text="Support")
    # places the button.
    btn1.place(relx=0.05+moveBtn, rely=0.42, relwidth=0.10, relheight=0.10)
    btn2.place(relx=0.16+moveBtn, rely=0.42, relwidth=0.10, relheight=0.10)
    btn3.place(relx=0.27+moveBtn, rely=0.42, relwidth=0.10, relheight=0.10)
    btn4.place(relx=0.38+moveBtn, rely=0.42, relwidth=0.10, relheight=0.10)
    btn5.place(relx=0.49+moveBtn, rely=0.42, relwidth=0.10, relheight=0.10)


def getWindow():
    print("test2")
    getTeams = tk.Button(Main_window, font=60, text="Get Teams", bg='grey', command=close_window)
    getTeams.place(relx=0.35, rely=0.4, relwidth=0.25, relheight=0.15)


# makes the program loop the main thread until exited
Main_window.mainloop()
