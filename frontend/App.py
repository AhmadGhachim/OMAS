import os.path
import tkinter as tk
from tkinter.filedialog import askopenfile

import sys

sys.path.append('..')

from backend import Main
from backend.DataProcessor import DataProcessor

root = tk.Tk()

canvas = tk.Canvas(root, width=640, height=480)
canvas.grid(columnspan=3, rowspan=3)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Meeting file", "*.csv")])
    if file:
        class_name = file.name.split('/')[-1].split('.')[0]
        path = os.path.abspath(os.path.pardir)
        path = path.replace("\\", "/", path.count("\\"))

        DataProcessor(path + "/backend/Excel files/" + class_name + '.xlsx', file.name, 'teams', 30, 0)
    browse_text.set("Upload meeting file")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button (root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#202020", fg="white", height=2, width=18)
browse_text.set ("Upload meeting file")
browse_btn.grid(column=1, row=2)

test_text = tk.StringVar()
test_btn = tk.Button(root, textvariable=test_text, command=lambda:Main, font="Raleway", bg="#202020", fg="white", height=2, width=18)
test_text.set("Run test script")
test_btn.grid(column=1, row=1)
root.mainloop()
