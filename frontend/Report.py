import tkinter
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import BOTH, BOTTOM, END, LEFT, RIGHT, Y, Frame, Listbox, Scrollbar, Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import window_width


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Report(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # create canvas
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 1000,
            width = 1500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        # add canvas to frame
        canvas.place(x=0, y=0)

        # create 'drop-down' button
        global drop_down_button_image
        drop_down_button_image = PhotoImage(
            file=relative_to_assets("button_1.png"))
        drop_down_button = Button(
            self,
            image=drop_down_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("drop_down_button clicked"),
            relief="flat"
        )

        # add 'drop-down' button to frame
        drop_down_button.place(
            x=599.0,
            y=1415.0,
            width=233.0,
            height=79.0
        )

        # create 'export' button
        global export_button_image
        export_button_image = PhotoImage(
            file=relative_to_assets("export.png"))
        export_button = Button(
            self,
            image=export_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("export_button clicked"),
            relief="flat"
        )

        # add 'export' button to frame
        export_button.place(
            x=418.0,
            y=833.0,
            width=260.0,
            height=50.0
        )

        # create 'view record' button

        value_inside_class = tkinter.StringVar(self)
        value_inside_class.set("Select an Option")
        viewRecord_button = Button(
            self,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("viewRecord_button clicked"),
            relief="flat"
        )

        # add 'view record' button to frame
        viewRecord_button.place(
            x=823.0,
            y=833.0,
            width=260.0,
            height=50.0
        )

        # import HomeScreen class
        from HomeScreen import HomeScreen

        # create 'go back' button
        global goBack_button_image
        goBack_button_image = PhotoImage(
            file=relative_to_assets("goBack.png"))
        goBack_button = Button(
            self,
            image=goBack_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(HomeScreen),
            relief="flat"
        )

        # add 'go back' button to frame
        goBack_button.place(
            x=109.0,
            y=89.0,
            width=125.0,
            height=50.0
        )

        # write text on canvas
        canvas.create_text(
            630.0,
            114.0,
            anchor="nw",
            text="Report for CMPT 370",
            fill="#000000",
            font=("Inter Medium", 36 * -1)
        )
