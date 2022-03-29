import os
import tkinter
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame

import HomeScreen

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
path = os.path.abspath(os.path.pardir)
path = path.replace("\\", "/", path.count("\\"))


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class ViewRecord(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 1000,
            width = 1500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            630.0,
            114.0,
            anchor="nw",
            text="View Record",
            fill="#000000",
            font=("Inter Medium", 36 * -1)
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
        value_inside_record = tkinter.StringVar(self)
        value_inside_record.set("Select an Option")
        try:
            class_options= [files[:-5] for files in os.listdir(path+"/backend/Excel files") if files[-5:] == ".xlsx"]
        except FileNotFoundError:
            class_options = [None]

        viewRecord= tkinter.OptionMenu(
            self,
            value_inside_record,
            *class_options,
        )


        viewRecord.place(
                x=442.0,
                y=199.0,
                width=374.0,
                height=50.0
            )

        global button_image_1
        button_image_1 = PhotoImage(
            file=relative_to_assets("openRecord.png"))
        button_1 = Button(
            self,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: os.startfile(path + "/backend/Excel files/"+value_inside_record.get()+".xlsx"),
            relief="flat"
        )
        button_1.place(
            x=859.0,
            y=199.0,
            width=200.0,
            height=50.0
        )

        global button_image_4
        button_image_4 = PhotoImage(
            file=relative_to_assets("monthAnalysis.png"))
        button_4 = Button(
            self,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=500.0,
            y=700.0,
            width=200.0,
            height=79.0
        )
        global button_image_5
        button_image_5 = PhotoImage(
            file=relative_to_assets("duration.png"))
        button_5 = Button(
            self,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=760.0,
            y=700.0,
            width=200.0,
            height=79.0
        )
