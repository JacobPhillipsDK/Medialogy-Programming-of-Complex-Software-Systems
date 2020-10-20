from tkinter import *
import tkinter as tk

btn_width = 20
btn_height = 20

root = Tk()
root.title("League of legends simulator game")
root.geometry("1500x720")
btncolor = '#884dbc'
background_label = tk.Label(root)

# creates a canvas for the application
canvas = tk.Canvas(root, width=1500, height=720, bg='#350f58', highlightthickness=0)


def frame1():
    return StartPage()


def frame2():
    return SecondPage()


def frame3():
    return SinglePLayerPage()


# packs in the canvas
canvas.pack()

frame1_btn1 = tk.Button(root, font=100, bg=btncolor, highlightthickness=0, bd='0', text="START", command=frame2)
frame2_btn1 = tk.Button(root, font=100, bg=btncolor, highlightthickness=0, bd='0', text="Single Player", command=frame3)
frame2_btn2 = tk.Button(root, font=100, bg=btncolor, highlightthickness=0, bd='0', text="MultiPlayer")
<<<<<<< HEAD
=======
frame3_btn1 = tk.Button(root, font=100, bg=btncolor, highlightthickness=0, bd='0', text="HELP ME")
>>>>>>> main


def StartPage():
    print("StartPage")
    frame1_btn1.place(relx=0.45, rely=0.42, relwidth=0.10, relheight=0.10)


def SecondPage():
    print("Second Page")
    frame1_btn1.destroy()
    frame2_btn1.place(relx=0.45, rely=0.3, relwidth=0.20, relheight=0.20)
    frame2_btn2.place(relx=0.45, rely=0.7, relwidth=0.20, relheight=0.20)


def SinglePLayerPage():
    print("ThirdPage")
    frame2_btn1.destroy()
    frame2_btn2.destroy()
    canvas.create_line(0, 100, 900, 100,width=5,fill="white")
    canvas.create_line(900, 1500, 900, 0,width=5,fill="white")
    canvas.create_line(0, 400, 900, 400, width=5,fill="white")


def close_window():
    root.destroy()


SinglePLayerPage()
root.mainloop()
