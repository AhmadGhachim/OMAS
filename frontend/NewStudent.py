import os
import sys
import tkinter
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, OptionMenu, messagebox
from tkinter import *

sys.path.append("../backend")

import HomeScreen
import WorkbookInitializer

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

global classOptions

side_text = []

student_fields = []

iterator = 0

class NewStudent(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        path = (os.path.abspath(os.path.pardir))
        path = path.replace("\\", "/", path.count("\\"))
        try:
            global classOptions
            classOptions = [file[0:-5] for file in os.listdir(path + "/backend/Excel files") if file[-5:] == ".xlsx"]
        except FileNotFoundError:
            tkinter.messagebox.showerror(title="Error", message="Please run 'Initialize Excel Databases' first")

        self.noOfStudents = 0
        self.mostFieldDimensionsY = {
            "student_count": 287,
            "entry_name": 276,
            "select_class": 276,
            "delete_button": 276,
            "addNewStudent": 367,
        }
        self.delete_buttons = []

        global side_text
        side_text = []

        global student_fields
        student_fields = []

        global iterator
        iterator = 0

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            bd=0,
            height=1000,
            width=1500,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas = canvas
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
            x=610.0,
            y=self.mostFieldDimensionsY["addNewStudent"],
            width=260.0,
            height=50.0
        )

        self.createNewStudent(canvas)


        def AddStudentProcessButton():
            count = 0
            success_count = 0
            success = list()
            errors = list()
            for student in student_fields:
                if str(globals()[f"select_class{student}"].get()) != "Select Class" and str(globals()[f"entry_name{student}"].get()) != "":
                    WorkbookInitializer.add_student(str(globals()[f"select_class{student}"].get()), str(globals()[f"entry_name{student}"].get()))
                    success_count += 1
                    success.append(count)
                else:
                    errors.append(count)
                count += 1
            if success_count:
                if success_count == 1:
                    tkinter.messagebox.showinfo(title="Success",
                                                message="Entry was added successfully!")
                else:
                    tkinter.messagebox.showinfo(title="Success",
                                                message=str(success_count) + " entries were added successfully!")
                if success_count == count:
                    master.switch_frame(HomeScreen.HomeScreen)
                else:
                    string = "Check inputs for student "
                    for x in range(len(errors)):
                        string += str(errors[x]+1)
                        if x == len(errors) - 2:
                            string += ' & '
                        else:
                            string += ", "
                    tkinter.messagebox.showwarning(title="Alert",
                                                   message= string[:-2])
                    success.reverse()
                    for x in success:
                        deleteButtons(self, x)
            else:
                tkinter.messagebox.showerror(title="Error", message="Invalid input(s), please try again.")

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
        global iterator

        # Don't need this anymore I guess
        # if self.noOfStudents > 0 and (None in [globals()[f"entry_name{student_fields[-1]}"]]or globals()[f"select_class{student_fields[-1]}"].get() not in classOptions):
        #     messagebox.showerror(title="warning", message="You cannot add another field while current one has not been filled completely")
        #     return

        if self.noOfStudents >= 1:
            addStudent.place_configure(x=610, y=self.mostFieldDimensionsY["addNewStudent"])

        self.noOfStudents += 1

        if self.noOfStudents == 5:
            addStudent.place_forget()

        student_fields.append(iterator)

        side_text.append(canvas.create_text(
            109.0,
            self.mostFieldDimensionsY["student_count"],
            anchor="nw",
            text="Student " + str(len(student_fields)),
            fill="#000000",
            font=("Roboto", 28 * -1)
        ))

        globals()[f"entry_name{iterator}"] = Entry(
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
        globals()[f"entry_name{iterator}"].place(
            x=276.0,
            y=self.mostFieldDimensionsY["entry_name"],
            width=600.0,
            height=48.0
        )
        globals()[f"select_class{iterator}"] = StringVar(self)
        globals()[f"select_class{iterator}"].set("Select Class")

        globals()[f"select_class_dropdown{iterator}"] = OptionMenu(
            self,
            globals()[f"select_class{iterator}"],
            *classOptions,
        )
        globals()[f"select_class_dropdown{iterator}"].place(
            x=930.0,
            y=self.mostFieldDimensionsY["select_class"],
            width=200.0,
            height=50.0
        )

        temp_button = Button(
            self,
            # image=deleteButtonImage,

            borderwidth=1,
            text= "X",
            bg= "red",
            fg= "white",
            highlightthickness=0,
            font=("Roboto", 25 * -1)
        )

        self.delete_buttons.append(temp_button)
        globals()[f"delete_button{iterator}"] = temp_button

        globals()[f"delete_button{iterator}"].configure(command=lambda: deleteButtons(self, self.delete_buttons.index(temp_button)))

        globals()[f"delete_button{iterator}"].place(
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

        iterator += 1

    global deleteButtons
    def deleteButtons(self, button_num):
        if self.noOfStudents > 1:
            global side_text
            self.canvas.delete(side_text[-1])
            side_text = side_text[:-1]

            self.delete_buttons.pop(button_num)

            globals()[f"entry_name{student_fields[button_num]}"].place_forget()
            globals()[f"select_class_dropdown{student_fields[button_num]}"].place_forget()
            globals()[f"delete_button{student_fields[button_num]}"].place_forget()

            self.mostFieldDimensionsY["student_count"] -= 97
            self.mostFieldDimensionsY["entry_name"] -= 97
            self.mostFieldDimensionsY["select_class"] -= 97
            self.mostFieldDimensionsY["delete_button"] -= 97
            self.mostFieldDimensionsY["addNewStudent"] -= 97

            for i in student_fields[button_num+1:]:
                globals()[f"entry_name{i}"].place_configure(y=int(globals()[f"entry_name{i}"].place_info()['y'])-97)

                globals()[f"select_class_dropdown{i}"].place_configure(y=int(globals()[f"select_class_dropdown{i}"].place_info()['y'])-97)

                globals()[f"delete_button{i}"].place(y=int(globals()[f"delete_button{i}"].place_info()['y'])-97)

            addStudent.place_configure(x= 610, y=self.mostFieldDimensionsY["addNewStudent"]-97)

            student_fields.pop(button_num)
            self.noOfStudents -= 1
        else:
            self.master.switch_frame(NewStudent)
