import tkinter as tk

HEIGHT = 1500
WIDTH = 1500
#Creates a window for the application.
Main_window = tk.Tk()
window = 1
Main_window.title("League simulator")


def vindueSkifter():
    print("test1")
    selectWindow()
    getWindow()
    matchWindow()
    print(window)

def close_window():
    Main_window.destroy()


#creates a canvas for the application
canvas = tk.Canvas(Main_window, height = HEIGHT, width = WIDTH)
#packs in the canvas
canvas.pack()

#background image for the startup.
#background_image = tk.PhotoImage(file='startImage.jpeg')
background_label = tk.Label(Main_window)

if window == 1:
    # creating a start button and inputs a text.
    Startbutton = tk.Button(Main_window, font=60, text="start", bg='grey', command = vindueSkifter)
    # places the button.
    Startbutton.place(relx=0.35, rely=0.4, relwidth=0.25, relheight=0.15)

def 
def getWindow():
    print("test2")
    getTeams = tk.Button(Main_window, font=60, text ="Get Teams", bg ='grey', command = close_window)
    getTeams.place(relx=0.35, rely=0.4, relwidth=0.25, relheight =0.15)

#makes the program loop the main thread until exited
Main_window.mainloop()
