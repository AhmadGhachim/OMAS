
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


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
    630.0,
    114.0,
    anchor="nw",
    text="View Record",
    fill="#000000",
    font=("Inter Medium", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("openRecord.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=859.0,
    y=199.0,
    width=200.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("goBack.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=109.0,
    y=89.0,
    width=125.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("recordDropDown.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=442.0,
    y=199.0,
    width=374.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("monthAnalysis.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=172.0,
    y=833.0,
    width=200.0,
    height=79.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("duration.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=491.0,
    y=833.0,
    width=200.0,
    height=79.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("studentAnalysisMonth.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=810.0,
    y=833.0,
    width=200.0,
    height=79.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("studentAnalysisDur.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=1129.0,
    y=833.0,
    width=200.0,
    height=79.0
)
window.resizable(False, False)
window.mainloop()
