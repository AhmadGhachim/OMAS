import os.path
import tkinter
from fileinput import filename
from pathlib import Path
import sys

sys.path.append("../backend")

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, OptionMenu, Toplevel, Frame
from tkinter import filedialog
from PIL import Image, ImageTk

import backend.DataProcessor
from backend.DataProcessor import DataProcessor
import NewStudent

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

path = os.path.abspath(os.path.pardir)
path = path.replace("\\", "/", path.count("\\"))


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class HomeScreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.filename = None
        self.cutoff = None
        self.meeting_service = None

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=1000,
            width=1500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_text(
            80.0,
            88.0,
            anchor="nw",
            text="OMAS ",
            fill="#000000",
            font=("Roboto", 72 * -1)
        )




        meetingDuration = Entry(
            self,
            borderwidth=0,
            highlightthickness=2,
            )
        meetingDuration.place(
            x=470.0,
            y=500.0,
            width=320.0,
            height=40.0
        )

        canvas.create_text(
            91.0,
            500.0,
            anchor="nw",
            text="Set Meeting Duration (in minutes)",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )


        cutOff = Entry(
            self,
            borderwidth=0,
            highlightthickness=2,
        )
        cutOff.place(
            x=470.0,
            y=587.0,
            width=320.0,
            height=40.0
        )

        canvas.create_text(
            91.0,
            587.0,
            anchor="nw",
            text="Set cutoff (in minutes)",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )


        serviceFile_Options= ["Zoom", "Webex", "Teams"]
        value_inside = tkinter.StringVar(self)
        value_inside.set("Select an Option")
        serviceFile = OptionMenu(
            self,
            value_inside,
            *serviceFile_Options,
        )
        serviceFile.place(
            x=470.0,
            y=670.0,
            width=320.0,
            height=40.0
        )

        canvas.create_text(
            91.0,
            670.0,
            anchor="nw",
            text="Select meeting service",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )
        #TODO Add Real Classes
        classOptions= ["Class 1", "Class 2"]
        value_inside = tkinter.StringVar(self)
        value_inside.set("Select an Option")
        classSelect = OptionMenu(
            self,
            value_inside,
            *classOptions,
        )
        classSelect.place(
            x=470.0,
            y=757.0,
            width=320.0,
            height=40.0
        )

        canvas.create_text(
            91.0,
            757.0,
            anchor="nw",
            text="Select Class",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )



        check = 'check-mark-button_2705.png'

        def UploadAction(event=None):
            filename = filedialog.askopenfilename()
            if filename:
                print('Selected:', filename)
                self.filename = filename
                uploadButtonImage.configure(file=relative_to_assets("check-mark-button_2705.png"))

        global uploadButtonImage
        uploadButtonImage = PhotoImage(
            file=relative_to_assets("DnD.png"))
        uploadButton = Button(
            image=uploadButtonImage,
            borderwidth=0,
            highlightthickness=0,
            text='Open',
            command=UploadAction,
            relief="flat"
        )
        uploadButton.place(
            x=865.0,
            y=500.0,
            width=555.0,
            height=298.0
        )

        canvas.create_text(
            1023.0,
            460.0,
            anchor="nw",
            text="Meeting service file ",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )

        global button_image_4
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

        # import the InitializeExcelDatabases class
        from InitialzeExcelDatabases import InitializeExcelDatabases

        global excelDatabaseNav_Image
        excelDatabaseNav_Image = PhotoImage(
            file=relative_to_assets("button_5.png"))
        excelDatabaseNav = Button(
            image=excelDatabaseNav_Image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(InitializeExcelDatabases),

            relief="flat"
        )
        excelDatabaseNav.place(
            x=1175.0,
            y=88.0,
            width=260.0,
            height=50.0
        )

        canvas.create_text(
            91.0,
            250.0,
            anchor="nw",
            text="An attendance system for online meeting platforms (Zoom, Teams etc.) which uses meeting reports "
                 "generated by\n"
                 "these services and automatically organises it in a database for the user.",
            fill="#000000",
            font=("Inter Regular", 24 * -1)
        )

        canvas.create_text(
            90.0,
            340.0,
            anchor="nw",
            text="1. Select a meeting service that matches your platform.\n"
                 "2. Upload the meeting service file provided by the platform.\n"
                 "3. Upload a .CSV file containg the student database.\n"
                 "4. Click the process button when steps 1 to 3 are done.",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )

        global processButton_Image
        processButton_Image = PhotoImage(
            file=relative_to_assets("process.png"))
        processButton = Button(
            image=processButton_Image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: call_data_processor(self.filename, int(cutOff.get()), value_inside.get()),
            relief="flat"
        )

        from Report import Report

        def call_data_processor(meeting_file: str = None, cut_off: int = None, service_type: str = None):

            if None in [meeting_file, cut_off, service_type]:
                tkinter.messagebox.showerror(title="warning", message="Not all details provided")
            else:
                dp = backend.DataProcessor.DataProcessor(path + "/backend/Excel files/CMPT 370.xlsx", meeting_file, service_type, 45, cut_off)
                dp.output_to_workbook()
                dp.output_to_text_file()
                dp.output_to_console()
                master.switch_frame(Report)

        processButton.place(
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

        global newStudentNav_Image
        newStudentNav_Image = PhotoImage(
            file=relative_to_assets("button_7.png"))
        newStudentNav = Button(
            image=newStudentNav_Image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(NewStudent.NewStudent),
            relief="flat"
        )
        newStudentNav.place(
            x=1175.0,
            y=164.0,
            width=260.0,
            height=50.0
        )
