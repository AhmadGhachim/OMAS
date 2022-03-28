import os
import tkinter
import tkinter
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, OptionMenu, messagebox
from tkinter import *

import HomeScreen

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
classOptions= ["Class 1", "Class 2"]

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

        self.noOfStudents = 0
        self.mostFieldDimensionsY = {
            "student_count": 287,
            "entry_name": 276,
            "select_class": 276,
            "delete_button": 276,
            "addNewStudent": 270,
        }


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
        self.createNewStudent(canvas)

        canvas.place(x=0, y=0)
        canvas.create_text(
            630.0,
            114.0,
            anchor="nw",
            text="Add new student",
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

        global addStudent_image
        addStudent_image = PhotoImage(
            file=relative_to_assets("addStudent.png"))
        global addStudent
        addStudent = Button(
            self,
            image=addStudent_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.createNewStudent(canvas),
            relief="flat"
        )
        addStudent.place(
            x=620.0,
            y=self.mostFieldDimensionsY["addNewStudent"],
            width=260.0,
            height=50.0
        )


        def AddStudentProcessButton():
            pass

        global processButton_Image
        processButton_Image = PhotoImage( file=relative_to_assets("process.png"))
        processButton = Button(
            image=processButton_Image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: AddStudentProcessButton(),
            relief="flat"
        )
        processButton.place(
            x=610.0,
            y=800.0,
            width=233.0,
            height=79.0
        )



    def createNewStudent(self, canvas):
        if self.noOfStudents > 0 and (None in [globals()[f"entry_name{self.noOfStudents}"]]or globals()[f"select_class{self.noOfStudents}"].get() not in classOptions):
            messagebox.showerror(title="warning", message="You cannot add another field while current one has not been filled completely")
            return

        if self.noOfStudents >= 1:
            addStudent.place_configure(x=610, y=self.mostFieldDimensionsY["addNewStudent"] + 90)

        self.noOfStudents += 1

        if self.noOfStudents == 5:
            addStudent.place_forget()

        canvas.create_text(
            109.0,
            self.mostFieldDimensionsY["student_count"],
            anchor="nw",
            text="Student " + str(self.noOfStudents),
            fill="#000000",
            font=("Roboto", 28 * -1)
        )

        globals()[f"entry_name{self.noOfStudents}"] = Entry(
            self,
            borderwidth=1,
            bd=0,
            bg="#FFFFFF",
            fg="#000000",
            insertbackground="#000000",
            highlightcolor="#fff",
            highlightthickness=2,
            relief="solid",
            font=("Roboto", 20 * -1)
        )
        globals()[f"entry_name{self.noOfStudents}"].place(
            x=276.0,
            y=self.mostFieldDimensionsY["entry_name"],
            width=600.0,
            height=48.0
        )
        globals()[f"select_class{self.noOfStudents}"] = StringVar(self)
        globals()[f"select_class{self.noOfStudents}"].set("Select Class")

        globals()[f"select_class_dropdown{self.noOfStudents}"] = OptionMenu(
            self,
            globals()[f"select_class{self.noOfStudents}"],
            #todo add real classes
            *classOptions,
        )
        globals()[f"select_class_dropdown{self.noOfStudents}"].place(
            x=930.0,
            y=self.mostFieldDimensionsY["select_class"],
            width=200.0,
            height=50.0
        )


        globals()[f"delete_button{self.noOfStudents}"] = Button(
            self,
            # image=deleteButtonImage,
            borderwidth=1,
            text= "X",
            bg= "red",
            fg= "white",
            highlightthickness=0,
            command= lambda: deleteButtons(self),
            font=("Roboto", 25 * -1)

        )
        globals()[f"delete_button{self.noOfStudents}"].place(
            x=1200.0,
            y=self.mostFieldDimensionsY["delete_button"],
            width=50.0,
            height=50.0
        )

        self.mostFieldDimensionsY["student_count"] += 97
        self.mostFieldDimensionsY["entry_name"] += 97
        self.mostFieldDimensionsY["select_class"] += 97
        self.mostFieldDimensionsY["delete_button"] += 97
        self.mostFieldDimensionsY["addNewStudent"] += 97

    global deleteButtons
    def deleteButtons(self):
        globals()[f"entry_name{self.noOfStudents}"].place_forget()
        globals()[f"select_class_dropdown{self.noOfStudents}"].place_forget()













