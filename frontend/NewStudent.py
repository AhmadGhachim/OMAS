import os
import tkinter
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame

import HomeScreen

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class NewStudent(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        path = (os.path.abspath(os.path.pardir))
        path = path.replace("\\", "/", path.count("\\"))
        try:
            # TODO: Classes for the dropdown menu
            classes = [file[0:-5] for file in os.listdir(path + "/backend/Excel files") if file[-5:] == ".xlsx"]
        except FileNotFoundError:
            tkinter.messagebox.showerror(title="Error", message="Please run 'Initialize Excel Databases' first")

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            bd=0,
            height=1000,
            width=1500,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        canvas.place(x=0, y=0)
        canvas.create_text(

            630.0,
            114.0,
            anchor="nw",
            text="Add new student",
            fill="#000000",
            font=("Inter Medium", 36 * -1)
        )

        global button_image_1
        button_image_1 = PhotoImage(
            file=relative_to_assets("addStudent.png"))
        button_1 = Button(
            self,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=620.0,
            y=515.0,
            width=260.0,
            height=50.0
        )

        global button_image_2
        button_image_2 = PhotoImage(
            file=relative_to_assets("goBack.png"))
        button_2 = Button(
            self,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(HomeScreen.HomeScreen),
            relief="flat"
        )
        button_2.place(
            x=109.0,
            y=89.0,
            width=125.0,
            height=50.0
        )

        canvas.create_text(

            109.0,
            287.0,
            anchor="nw",
            text="Student 1",
            fill="#000000",
            font=("Roboto", 28 * -1)
        )

        global entry_image_1
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            721.0,
            301.0,
            image=entry_image_1
        )
        entry_1 = Text(
            self,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=1
        )
        entry_1.place(
            x=276.0,
            y=276.0,
            width=890.0,
            height=48.0
        )

        global button_image_3
        button_image_3 = PhotoImage(
            file=relative_to_assets("dropDown.png"))
        button_3 = Button(
            self,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=1192.0,
            y=276.0,
            width=200.0,
            height=50.0
        )

        canvas.create_text(

            1270.0,
            294.0,
            anchor="nw",
            text="class",
            fill="#000000",
            font=("Inter Medium", 18 * -1)
        )

        canvas.create_text(

            108.0,
            384.0,
            anchor="nw",
            text="Student 2",
            fill="#000000",
            font=("Roboto", 28 * -1)
        )

        global entry_image_2
        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            720.0,
            398.0,
            image=entry_image_2
        )
        entry_2 = Text(
            self,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=1
        )
        entry_2.place(
            x=275.0,
            y=373.0,
            width=890.0,
            height=48.0
        )

        global button_image_4
        button_image_4 = PhotoImage(
            file=relative_to_assets("dropDown.png"))
        button_4 = Button(
            self,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=1191.0,
            y=373.0,
            width=200.0,
            height=50.0
        )

        canvas.create_text(

            1270.0,
            391.0,
            anchor="nw",
            text="class",
            fill="#000000",
            font=("Inter Medium", 18 * -1)
        )
