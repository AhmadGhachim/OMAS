from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1500x1000")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1000,
    width=1500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=599.0,
    y=1415.0,
    width=233.0,
    height=79.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("export.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=418.0,
    y=833.0,
    width=260.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("viewRecord.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=823.0,
    y=833.0,
    width=260.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("goBack.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=109.0,
    y=89.0,
    width=125.0,
    height=50.0
)

canvas.create_text(
    630.0,
    114.0,
    anchor="nw",
    text="Report for CMPT 370",
    fill="#000000",
    font=("Inter Medium", 36 * -1)
)
window.resizable(False, False)
window.mainloop()
