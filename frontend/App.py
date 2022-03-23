import tkinter
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, OptionMenu
from tkinter import filedialog
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1500x1000")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1000,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    80.0,
    88.0,
    anchor="nw",
    text="OMAS ",
    fill="#000000",
    font=("Roboto", 72 * -1)
)

serviceFile_Options= ["Zoom", "Webex", "Teams"]
value_inside = tkinter.StringVar(window)
value_inside.set("Select an Option")
serviceFile = OptionMenu(
    window,
    value_inside,
    *serviceFile_Options,
)
serviceFile.place(
    x=445.0,
    y=640.0,
    width=320.0,
    height=40.0
)

# button_image_2 = PhotoImage(
#     file=relative_to_assets("button_2.png"))
cutOff = Entry(
    # image=button_image_2,
    borderwidth=0,
    highlightthickness=2,
    # command=lambda: print("button_2 clicked"),
    # relief="flat"

)
cutOff.place(
    x=445.0,
    y=546.0,
    width=320.0,
    height=40.0
)

canvas.create_text(
    91.0,
    641.0,
    anchor="nw",
    text="Select meeting service",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    91.0,
    641.0,
    anchor="nw",
    text="Select meeting service",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    91.0,
    549.0,
    anchor="nw",
    text="Set cutoff (in minutes)",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    1023.0,
    381.0,
    anchor="nw",
    text="Meeting service file ",
    fill="#000000",
    font=("Roboto", 24 * -1)
)
check = 'check-mark-button_2705.png'
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    button_image_3.configure(file=relative_to_assets("check-mark-button_2705.png"))


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    text='Open',
    command=UploadAction,
    relief="flat"
)
button_3.place(
    x=865.0,
    y=426.0,
    width=555.0,
    height=298.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=599.0,
    y=1415.0,
    width=233.0,
    height=79.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=1175.0,
    y=88.0,
    width=260.0,
    height=50.0
)

canvas.create_text(
    91.0,
    250.0,
    anchor="nw",
    text="An attendance system for online meeting platforms (Zoom, Teams etc.) which uses meeting reports generated by\n"
         "these services and automatically organises it in a database for the user.",
    fill="#000000",
    font=("Inter Regular", 24 * -1)
)

canvas.create_text(
    80.0,
    340.0,
    anchor="nw",
    text="1. Select a meeting service that matches your platform.\n"
         "2. Upload the meeting service file provided by the platform.\n"
         "3. Upload a .CSV file containg the student database.\n"
         "4. Click the process button when steps 1 to 3 are done.",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=634.0,
    y=833.0,
    width=233.0,
    height=79.0
)

canvas.create_text(
    296.0,
    122.0,
    anchor="nw",
    text="Online Meetings Attendance System",
    fill="#000000",
    font=("Roboto", 36 * -1)
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=1175.0,
    y=164.0,
    width=260.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()

