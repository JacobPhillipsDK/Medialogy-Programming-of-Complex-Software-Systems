from tkinter import *
import tkinter as tk


def raise_frame(frame):
    frame.tkraise()


btn_width = 20
btn_height = 20
frame = 1
root = Tk()
root.title("League of legends simulator game")
root.geometry("1500x720")
btncolor = '#884dbc'


def close_window():
    root.destroy()


# creates a canvas for the application
canvas = tk.Canvas(root, width=1500, height=720, bg='#350f58', highlightthickness=0)
# packs in the canvas
canvas.pack()

moveBtn = 0.2

background_label = tk.Label(root)

if frame == 1:
    # creating a start button and inputs a text.
    frame1_btn1 = tk.Button(root, font=100, bg=btncolor, highlightthickness=0, bd='0', text="START",
                            command=frame == 2)
    # places the button.
    frame1_btn1.place(relx=0.45, rely=0.42, relwidth=0.10, relheight=0.10)

if frame == 2:
    frame2_btn1 = tk.Button(root, font=100, bg=btncolor, highlightthickness=0, bd='0', text="Single Player")
    frame2_btn2 = tk.Button(root, font=100, bg=btncolor, highlightthickness=0, bd='0', text="MultiPlayer")
    frame2_btn1.place(relx=0.45, rely=0.42, relwidth=0.10, relheight=0.10)
    frame2_btn1.place(relx=0.75, rely=0.42, relwidth=0.10, relheight=0.10)



def frame1():


def frame2():




# makes the program loop the main thread until exited
root.mainloop()
