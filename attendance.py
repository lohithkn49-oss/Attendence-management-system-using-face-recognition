import tkinter as tk
from tkinter import *
import os
import cv2
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import pyttsx3

# project modules
import show_attendance
import takeImage
import trainImage
import automaticAttedance


# -------------------- TEXT TO SPEECH --------------------

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


# -------------------- PATHS --------------------

haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "./TrainingImageLabel/Trainner.yml"
trainimage_path = "./TrainingImage"
studentdetail_path = "./StudentDetails/studentdetails.csv"
attendance_path = "./Attendance"

# create folders if not exist
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

if not os.path.exists("TrainingImageLabel"):
    os.makedirs("TrainingImageLabel")

if not os.path.exists("StudentDetails"):
    os.makedirs("StudentDetails")

if not os.path.exists(attendance_path):
    os.makedirs(attendance_path)


# -------------------- MAIN WINDOW --------------------

window = Tk()
window.title("Face Recognition Attendance System")
window.geometry("1280x720")
window.configure(background="#1c1c1c")

# -------------------- HEADER --------------------

title = tk.Label(
    window,
    text="CLASS VISION",
    bg="#1c1c1c",
    fg="yellow",
    font=("Verdana", 30, "bold")
)
title.pack(pady=20)

welcome = tk.Label(
    window,
    text="Welcome to Face Recognition Attendance System",
    bg="#1c1c1c",
    fg="yellow",
    font=("Verdana", 25, "bold")
)
welcome.pack()


# -------------------- ERROR WINDOW --------------------

def err_screen():
    sc1 = tk.Toplevel()
    sc1.geometry("300x100")
    sc1.title("Warning")
    sc1.configure(background="#1c1c1c")

    tk.Label(
        sc1,
        text="Enrollment & Name required!",
        fg="yellow",
        bg="#1c1c1c",
        font=("Verdana", 12, "bold")
    ).pack(pady=10)

    tk.Button(
        sc1,
        text="OK",
        command=sc1.destroy,
        bg="black",
        fg="yellow"
    ).pack()


# -------------------- REGISTER STUDENT WINDOW --------------------

def TakeImageUI():

    ImageUI = Toplevel()
    ImageUI.title("Register Student")
    ImageUI.geometry("600x400")
    ImageUI.configure(background="#1c1c1c")

    heading = Label(
        ImageUI,
        text="Register Student Face",
        bg="#1c1c1c",
        fg="yellow",
        font=("Verdana", 22, "bold")
    )
    heading.pack(pady=20)

    # Enrollment
    lbl1 = Label(ImageUI, text="Enrollment No", bg="#1c1c1c", fg="yellow")
    lbl1.pack()

    txt1 = Entry(ImageUI, width=25)
    txt1.pack(pady=5)

    # Name
    lbl2 = Label(ImageUI, text="Name", bg="#1c1c1c", fg="yellow")
    lbl2.pack()

    txt2 = Entry(ImageUI, width=25)
    txt2.pack(pady=5)

    message = Label(ImageUI, text="", bg="#1c1c1c", fg="yellow")
    message.pack(pady=10)

    def take_image():
        Id = txt1.get()
        name = txt2.get()

        if Id == "" or name == "":
            err_screen()
        else:
            takeImage.TakeImage(
                Id,
                name,
                haarcasecade_path,
                trainimage_path,
                message,
                err_screen,
                text_to_speech
            )

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech
        )

    Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bg="black",
        fg="yellow",
        width=15
    ).pack(pady=10)

    Button(
        ImageUI,
        text="Train Images",
        command=train_image,
        bg="black",
        fg="yellow",
        width=15
    ).pack()


# -------------------- ATTENDANCE FUNCTIONS --------------------

def automatic_attendance():
    automaticAttedance.subjectChoose(text_to_speech)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


# -------------------- MAIN BUTTONS --------------------

Button(
    window,
    text="Register New Student",
    command=TakeImageUI,
    bg="black",
    fg="yellow",
    width=20,
    height=2
).place(x=150, y=400)

Button(
    window,
    text="Take Attendance",
    command=automatic_attendance,
    bg="black",
    fg="yellow",
    width=20,
    height=2
).place(x=520, y=400)

Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bg="black",
    fg="yellow",
    width=20,
    height=2
).place(x=900, y=400)

Button(
    window,
    text="Exit",
    command=quit,
    bg="black",
    fg="yellow",
    width=20,
    height=2
).place(x=520, y=500)


window.mainloop()
