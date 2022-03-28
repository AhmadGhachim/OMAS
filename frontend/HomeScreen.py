import os.path
import tkinter
from fileinput import filename
from pathlib import Path
import sys

import ViewRecord

sys.path.append("../backend")

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, OptionMenu, Toplevel, Frame
from tkinter import filedialog
#from PIL import Image, ImageTk

import DataProcessor
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
            67.0,
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
            y=570.0,
            width=320.0,
            height=40.0
        )

        canvas.create_text(
            91.0,
            570.0,
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
            y=657.0,
            width=320.0,
            height=40.0
        )

        canvas.create_text(
            91.0,
            657.0,
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
            y=487.0,
            width=320.0,
            height=40.0
        )

        canvas.create_text(
            91.0,
            487.0,
            anchor="nw",
            text="Select meeting service",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )

        #TODO Add Real Classes
        classOptions= ["Class 1", "Class 2"]
        value_inside_class = tkinter.StringVar(self)
        value_inside_class.set("Select an Option")
        classSelect = OptionMenu(
            self,
            value_inside_class,
            *classOptions,
        )
        classSelect.place(
            x=470.0,
            y=400.0,
            width=320.0,
            height=40.0
        )

        canvas.create_text(
            91.0,
            400.0,
            anchor="nw",
            text="Select Class",
            fill="#000000",
            font=("Roboto", 24 * -1)
        )


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
            y=400.0,
            width=450.0,
            height=290.0
        )

        canvas.create_text(
            990.0,
            360.0,
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
            x=970.0,
            y=88.0,
            width=260.0,
            height=50.0
        )

        canvas.create_text(
            91.0,
            210.0,
            anchor="nw",
            text="An attendance system for online meeting platforms (Zoom, Teams etc.)\nwhich uses meeting reports"
                 "generated by"
                 "these services\nand automatically organises it in a database for the user.",
            fill="#000000",
            font=("Inter Regular", 24 * -1)
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
                print(service_type)
                dp = DataProcessor.DataProcessor(path + "/backend/Excel files/CMPT 370.xlsx", meeting_file, service_type, 45, cut_off)
                dp.output_to_workbook()
                dp.output_to_text_file()
                dp.output_to_console()
                master.switch_frame(Report)

        processButton.place(
            x=560.0,
            y=750.0,
            width=233.0,
            height=79.0
        )

        canvas.create_text(
            296.0,
            95.0,
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
            x=970.0,
            y=164.0,
            width=260.0,
            height=50.0
        )

        global viewRecordsHome_Image
        viewRecordsHome_Image = PhotoImage(
        file=relative_to_assets("viewRecordsHome.png"))
        viewRecordsHome = Button(
            image=viewRecordsHome_Image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(ViewRecord.ViewRecord),
            relief="flat"
        )
        viewRecordsHome.place(
            x=970.0,
            y=244.0,
            width=260.0,
            height=50.0
        )

        def callback(input):
            if input.isdigit():
                return True

            elif input is "":
                return True

            else:
                return False

        reg = self.register(callback)

        meetingDuration.config(validate="key", validatecommand=(reg, '%P'))
        cutOff.config(validate="key", validatecommand=(reg, '%P'))



