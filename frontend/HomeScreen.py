import os.path
import tkinter
from fileinput import filename
from pathlib import Path
import sys

import ViewRecord

sys.path.append("../backend")
import DataProcessor

from InitialzeExcelDatabases import InitializeExcelDatabases

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, OptionMenu, Toplevel, Frame
from tkinter import filedialog
from PIL import Image, ImageTk

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

        try:
            class_options= [files[:-5] for files in os.listdir(path+"/backend/Excel files") if files[-5:] == ".xlsx"]
        except FileNotFoundError:
            class_options = [None]
        value_inside_class = tkinter.StringVar(self)
        value_inside_class.set("Select an Option")
        classSelect = OptionMenu(
            self,
            value_inside_class,
            *class_options,
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
            filename = filedialog.askopenfilename(filetypes=[('Meeting files', '*csv')])
            if filename:
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

        if class_options == [None]:
            canvas.create_text(
                91.0,
                320.0,
                anchor="nw",
                text="Please click on 'Initialze Excel Databases'",
                fill='#ff0000',
                font=("Inter Regular", 24 * -1)
            )




        global processButton_Image
        processButton_Image = PhotoImage(
            file=relative_to_assets("process.png"))
        processButton = Button(
            image=processButton_Image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: call_data_processor(value_inside_class.get(), self.filename, meetingDuration.get(), cutOff.get(), value_inside.get()),
            relief="flat"
        )

        from Report import Report

        def call_data_processor(class_name: str = None, meeting_file: str = None, duration = None, cut_off= None, service_type: str = None):
            if class_options == [None]:
                tkinter.messagebox.showerror(title="Warning", message="Excel databases not initialized")
            else:
                try:
                    cut_off = int(cut_off)
                except ValueError:
                    tkinter.messagebox.showerror(title="Incorrect cutoff duration", message="Cutoff duration should be a number")

                try:
                    duration = int(duration)
                except ValueError:
                    tkinter.messagebox.showerror(title="Incorrect meeting duration", message="Meeting duration should be a number")

                if None in [class_name, meeting_file, cut_off, service_type]:
                    tkinter.messagebox.showerror(title="Warning", message="Not all details provided")
                else:
                    print(service_type)
                    dp = DataProcessor.DataProcessor(path + "/backend/Excel files/"+ class_name +".xlsx", meeting_file, service_type, duration, cut_off)
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

            elif input == "":
                return True

            else:
                return False

        reg = self.register(callback)

        meetingDuration.config(validate="key", validatecommand=(reg, '%P'))
        cutOff.config(validate="key", validatecommand=(reg, '%P'))



