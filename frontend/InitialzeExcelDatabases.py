from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Frame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class InitializeExcelDatabases(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

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

        global button_image_1
        button_image_1 = PhotoImage(
            file=relative_to_assets("uploadList.png"))
        button_1 = Button(
            self,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=1092.0,
            y=276.0,
            width=300.0,
            height=50.0
        )

        canvas.create_text(
            109.0,
            287.0,
            anchor="nw",
            text="Class 1",
            fill="#000000",
            font=("Roboto", 28 * -1)
        )

        # entry_image_1 = PhotoImage(
        #     file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            436.0,
            301.0,
            # image=entry_image_1
        )
        entry_1 = Text(
            self,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=2
        )
        entry_1.place(
            x=276.0,
            y=276.0,
            width=320.0,
            height=48.0
        )

        canvas.create_text(
            525.0,
            109.0,
            anchor="nw",
            text="Initialze Excel Databases",
            fill="#000000",
            font=("Inter Medium", 36 * -1)
        )

        global button_image_2
        button_image_2 = PhotoImage(
            file=relative_to_assets("addNewClass.png"))
        button_2 = Button(
            self,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=650.0,
            y=515.0,
            width=200.0,
            height=50.0
        )

        # import the HomeScreen class
        from HomeScreen import HomeScreen

        global button_image_3
        button_image_3 = PhotoImage(
            file=relative_to_assets("goBack.png"))
        button_3 = Button(
            self,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(HomeScreen),
            relief="flat"
        )
        button_3.place(
            x=109.0,
            y=89.0,
            width=125.0,
            height=50.0
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
            x=628.0,
            y=276.0,
            width=200.0,
            height=50.0
        )

        global button_image_5
        button_image_5 = PhotoImage(
            file=relative_to_assets("dropDown.png"))
        button_5 = Button(
            self,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=860.0,
            y=276.0,
            width=200.0,
            height=50.0
        )

        global button_image_6
        button_image_6 = PhotoImage(
            file=relative_to_assets("uploadList.png"))
        button_6 = Button(
            self,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=1092.0,
            y=373.0,
            width=300.0,
            height=50.0
        )

        canvas.create_text(
            109.0,
            384.0,
            anchor="nw",
            text="Class 2",
            fill="#000000",
            font=("Roboto", 28 * -1)
        )

        # entry_image_2 = PhotoImage(
        #     file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            436.0,
            398.0,
            # image=entry_image_2
        )
        entry_2 = Text(
            self,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=2
        )
        entry_2.place(
            x=276.0,
            y=373.0,
            width=320.0,
            height=48.0
        )

        global button_image_7
        button_image_7 = PhotoImage(
            file=relative_to_assets("dropDown.png"))
        button_7 = Button(
            self,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        button_7.place(
            x=628.0,
            y=373.0,
            width=200.0,
            height=50.0
        )

        global button_image_8
        button_image_8 = PhotoImage(
            file=relative_to_assets("dropDown.png"))
        button_8 = Button(
            self,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        button_8.place(
            x=860.0,
            y=373.0,
            width=200.0,
            height=50.0
        )

        global button_image_9
        button_image_9 = PhotoImage(
            file=relative_to_assets("process.png"))
        button_9 = Button(
            self,
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        button_9.place(
            x=634.0,
            y=858.0,
            width=233.0,
            height=79.0
        )
