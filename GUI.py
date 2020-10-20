from tkinter import *

window = Tk()
window.geometry('1500x720')
moveBtn = 0.2

startFrame = Frame(window)
selectMode = Frame(window)
getTeams = Frame(window)
playerSelect = Frame(window)
simMatch = Frame(window)
results = Frame(window)


def swap(frame):
    frame.tkraise()


for frame in (startFrame, selectMode, getTeams, simMatch, results):
    frame.grid(row = 0, column = 0)

Label(startFrame, text="Starting frame").pack()
Button(startFrame, text="start", command = lambda: swap(selectMode)).pack()

Label(selectMode, text="Select mode").pack
Button(selectMode, text = "Singleplayer",command = lambda: swap(getTeams)).pack()
Button(selectMode, text = "multiplayer",command = lambda: swap(getTeams)).pack()


Label(getTeams, text = "Get teams").pack
Button(getTeams, text = "get teams", command = lambda: swap(playerSelect)).pack()
startFrame.tkraise()

Label(playerSelect, text = "select players").pack

    btn1 = Tk.Button(window, font=100, bg=btncolor, highlightthickness=0, bd='0', text="Top")
    btn2 = Tk.Button(window, font=100, bg=btncolor, highlightthickness=0, bd='0', text="Jungle")
    btn3 = Tk.Button(window, font=100, bg=btncolor, highlightthickness=0, bd='0', text="Mid")
    btn4 = Tk.Button(window, font=100, bg=btncolor, highlightthickness=0, bd='0', text="ADC")
    btn5 = Tk.Button(window, font=100, bg=btncolor, highlightthickness=0, bd='0', text="Support")
    # places the button.
    btn1.place(relx=0.05+moveBtn, rely=0.42, relwidth=0.10, relheight=0.10)
    btn2.place(relx=0.16+moveBtn, rely=0.42, relwidth=0.10, relheight=0.10)
    btn3.place(relx=0.27+moveBtn, rely=0.42, relwidth=0.10, relheight=0.10)
    btn4.place(relx=0.38+moveBtn, rely=0.42, relwidth=0.10, relheight=0.10)
    btn5.place(relx=0.49+moveBtn, rely=0.42, relwidth=0.10, relheight=0.10)



window.mainloop()

# Creates a window for the application.

# root = tk.Tk()
# root.title("League simulator")


# class SampleApp(tk.Tk):
#  def __init__(self):
# tk.Tk.__init__(self)
# self._frame = None
# self.switch_frame(startPage)

# def switch_frame(self, frame_class):
# new_frame = frame_class(self)
# if self._frame is not None:
#     self._frame.destroy()
# self._frame = new_frame
#        self._frame.pack()


# def close_window():
#  root.destroy()


# creates a canvas for the application
# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# packs in the canvas
# canvas.pack()

# background image for the startup.
# background_image = tk.PhotoImage(file='startImage.jpeg')
# background_label = tk.Label(root)


# class startPage(tk.Frame):
# def __init__(self, master):

# creating a start button and inputs a text.
# Startbutton = tk.Button(root, font=60, text="start", bg='grey', command=close_window)
# places the button.
# Startbutton.place(relx=0.35, rely=0.4, relwidth=0.25, relheight=0.15)


# class choseMode(tk.frame):
#  def __init__(self):


# class getWindow(tk.Frame):
# def __init__(self):
# getTeams = tk.Button(root, font=60, text="Get Teams", bg='grey', command=close_window)
# getTeams.place(relx=0.35, rely=0.4, relwidth=0.25, relheight=0.15)


# makes the program loop the main thread until exited
