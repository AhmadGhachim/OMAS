import tkinter.messagebox
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Frame, StringVar, OptionMenu
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import sys

from backend import WorkbookInitializer
from backend.WorkbookInitializer import workbook_initializer
from frontend.NewStudent import side_text

sys.path.append("../backend")
sys.path.append("../Test files")

# from WorkbookInitializer import workbook_initializer



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


month_Options= ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']

side_text_wb = []

class_fields = []

iterator_wb = 0


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class InitializeExcelDatabases(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.noOfClasses = 0
        self.mostFieldDimensionsY = {
            "canvas_text": 287, 
            "entry_text": 276, 
            "start_month": 276, 
            "end_month": 276, 
            "uploadClassList": 276, 
            "addNewClass": 400,
            "deleteWorkbook": 276
        }

        self.delete_workbook_buttons = []
        self.upload_txt_file_buttons = []

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

        global side_text_wb
        side_text_wb = []

        global class_fields
        class_fields = []

        global iterator_wb
        iterator_wb = 0

        canvas.create_text(
            500.0,
            109.0,
            anchor="nw",
            text="Initialize Excel Databases",
            fill="#000000",
            font=("Inter Medium", 36 * -1)
        )


        global addNewClass_button_image
        addNewClass_button_image = PhotoImage(
            file=relative_to_assets("addNewClass.png"))
        global addNewClass_button
        addNewClass_button = Button(
            self,
            image=addNewClass_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.createNewField(canvas),
            relief="flat"
        )
        addNewClass_button.place(
            x=595.0,
            y=self.mostFieldDimensionsY["addNewClass"],
            width=200.0,
            height=50.0
        )

        # import the HomeScreen class
        from HomeScreen import HomeScreen

        global goBack_button_image
        goBack_button_image = PhotoImage(
            file=relative_to_assets("goBack.png"))
        goBack_button = Button(
            self,
            image=goBack_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: master.switch_frame(HomeScreen),
            relief="flat"
        )
        goBack_button.place(
            x=80.0,
            y=89.0,
            width=125.0,
            height=50.0
        )

        self.createNewField(canvas)


        # initialize workbook
        def initializeWorkbookDatabase():
            count = 0
            success_count = 0
            success = list()
            errors = list()
            for classes in class_fields:
                if str(globals()[f"class_name_entry{classes}"].get()) != "" and str(globals()[f"start_month{classes}"].get()) != "Select class start period" and str(globals()[f"end_month{classes}"].get()) != "Select class end period" and globals()[f"filename{classes}"] is not None:
                    WorkbookInitializer.workbook_initializer(globals()[f"class_name_entry{classes}"].get(), (globals()[f"start_month{classes}"].get(), globals()[f"end_month{classes}"].get()), globals()[f"filename{classes}"])
                    success_count += 1
                    success.append(count)
                else:
                    errors.append(count)
                count += 1
            if success_count:
                if success_count == 1:
                    tkinter.messagebox.showinfo(title="Success",
                                                message="Database was created successfully!")
                else:
                    tkinter.messagebox.showinfo(title="Success",
                                                message=str(success_count) + " databases were created successfully!")

                if success_count == count:
                    master.switch_frame(HomeScreen)
                else:
                    string = "Check inputs for class "
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
                        deleteWorkbookButtons(self, x)
            else:
                tkinter.messagebox.showerror(title="Error", message="Invalid input(s), please try again.")
        ######################################################################################


        global process_button_image
        process_button_image = PhotoImage(
            file=relative_to_assets("process.png"))
        process_button = Button(
            self,
            image=process_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: initializeWorkbookDatabase(),
            relief="flat"
        )
        process_button.place(
            x=580.0,
            y=800.0,
            width=233.0,
            height=79.0
        )


    def createNewField(self, canvas):
        global iterator_wb

        # if self.noOfClasses > 0 and ( None in [globals()[f"filename{self.noOfClasses}"], globals()[f"class_name_entry{self.noOfClasses}"]] or globals()[f"start_month{self.noOfClasses}"].get() not in month_Options or globals()[f"end_month{self.noOfClasses}"].get() not in month_Options):
        #     messagebox.showerror(title="warning", message="You cannot add another field while current one has not been filled completely")
        #     return

        if self.noOfClasses >= 1:
            addNewClass_button.place_configure(x=595, y=self.mostFieldDimensionsY["addNewClass"])

        self.noOfClasses += 1

        if self.noOfClasses == 5:
            addNewClass_button.place_forget()

        class_fields.append(iterator_wb)


        # to upload class list
        def UploadAction(button_num):
            globals()[f"filename{button_num}"] = filedialog.askopenfilename(filetypes=[('Text files', '*txt')])
            if globals()[f"filename{button_num}"] and globals()[f"uploadList_button{button_num}"]:
                print('Selected:', globals()[f"filename{button_num}"])
                self.upload_txt_file_buttons[button_num].configure(text=globals()[f"filename{button_num}"].split("/")[-1])
                globals()[f"class_name_entry{class_fields[button_num]}"].delete(0, END)
                globals()[f"class_name_entry{class_fields[button_num]}"].insert(END, (globals()[f"filename{button_num}"].split("/")[-1][0:-4]))
        #####################################################


        temp_upload = Button(
            self,
            text="+  Upload Student Name List",
            borderwidth=0,
            highlightthickness=0,
            font=("Roboto", 20 * -1),
            relief="flat",
            bg="#fff"
        )

        self.upload_txt_file_buttons.append(temp_upload)

        globals()[f"uploadList_button{iterator_wb}"] = temp_upload

        globals()[f"uploadList_button{iterator_wb}"].configure(command=lambda: UploadAction(self.upload_txt_file_buttons.index(temp_upload)))

        globals()[f"uploadList_button{iterator_wb}"].place(
            x=920.0,
            y=self.mostFieldDimensionsY["uploadClassList"],
            width=300.0,
            height=50.0
        )
        globals()[f"filename{iterator_wb}"] = None # associate a file path with a new row of fields

        side_text_wb.append(
            canvas.create_text(
            80.0,
            self.mostFieldDimensionsY["canvas_text"],
            anchor="nw",
            text="Class " + str(len(class_fields)),
            fill="#000000",
            font=("Roboto", 28 * -1)
        ))

        globals()[f"class_name_entry{iterator_wb}"] = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000000",
            insertbackground="#000000",
            highlightcolor="#fff",
            highlightthickness=2,
            font=("Roboto", 20 * -1)
        )
        globals()[f"class_name_entry{iterator_wb}"].place(
            x=180.0,
            y=self.mostFieldDimensionsY["entry_text"],
            width=320.0,
            height=48.0
        )


        globals()[f"start_month{iterator_wb}"] = StringVar(self)
        globals()[f"end_month{iterator_wb}"] = StringVar(self)
        globals()[f"start_month{iterator_wb}"].set("Select class start period")
        globals()[f"end_month{iterator_wb}"].set("Select class end period")


        globals()[f"start_month_dropdown{iterator_wb}"] = OptionMenu(
            self,
            globals()[f"start_month{iterator_wb}"],
            *month_Options,
            # command=lambda: print("button_4 clicked"),
        )
        globals()[f"start_month_dropdown{iterator_wb}"].place(
            x=510.0,
            y=self.mostFieldDimensionsY["start_month"],
            width=200.0,
            height=50.0
        )


        globals()[f"end_month_dropdown{iterator_wb}"] = OptionMenu(
            self,
            globals()[f"end_month{iterator_wb}"],
            *month_Options,
            # command=lambda: print("button_4 clicked"),
        )
        globals()[f"end_month_dropdown{iterator_wb}"].place(
            x=710.0,
            y=self.mostFieldDimensionsY["start_month"],
            width=200.0,
            height=50.0
        )

        temp_button = Button(
            self,
            borderwidth=1,
            text="X",
            bg="red",
            fg="white",
            highlightthickness=0,
            font=("Roboto", 25 * -1)
        )

        self.delete_workbook_buttons.append(temp_button)
        globals()[f"delete_workbook_buttons{iterator_wb}"] = temp_button

        globals()[f"delete_workbook_buttons{iterator_wb}"].configure(command=lambda: deleteWorkbookButtons(self, self.delete_workbook_buttons.index(temp_button)))

        globals()[f"delete_workbook_buttons{iterator_wb}"].place(
            x=1250.0,
            y=self.mostFieldDimensionsY["deleteWorkbook"],
            width=50.0,
            height=50.0
        )

        self.mostFieldDimensionsY["canvas_text"] += 97
        self.mostFieldDimensionsY["entry_text"] += 97
        self.mostFieldDimensionsY["start_month"] += 97
        self.mostFieldDimensionsY["end_month"] += 97
        self.mostFieldDimensionsY["uploadClassList"] += 97
        self.mostFieldDimensionsY["addNewClass"] += 97
        self.mostFieldDimensionsY["deleteWorkbook"] += 97

        iterator_wb += 1

    global deleteWorkbookButtons
    def deleteWorkbookButtons(self, button_num):
        if self.noOfClasses > 1:
            global side_text_wb
            self.canvas.delete(side_text_wb[-1])
            side_text_wb = side_text_wb[:-1]

            self.delete_workbook_buttons.pop(button_num)
            self.upload_txt_file_buttons.pop(button_num)

            globals()[f"class_name_entry{class_fields[button_num]}"].place_forget()
            globals()[f"start_month_dropdown{class_fields[button_num]}"].place_forget()
            globals()[f"end_month_dropdown{class_fields[button_num]}"].place_forget()
            globals()[f"uploadList_button{class_fields[button_num]}"].place_forget()
            globals()[f"delete_workbook_buttons{class_fields[button_num]}"].place_forget()

            self.mostFieldDimensionsY["canvas_text"] -= 97
            self.mostFieldDimensionsY["entry_text"] -= 97
            self.mostFieldDimensionsY["start_month"] -= 97
            self.mostFieldDimensionsY["end_month"] -= 97
            self.mostFieldDimensionsY["uploadClassList"] -= 97
            self.mostFieldDimensionsY["addNewClass"] -= 97
            self.mostFieldDimensionsY["deleteWorkbook"] -= 97

            for i in class_fields[button_num+1:]:
                globals()[f"class_name_entry{i}"].place_configure(y=int(globals()[f"class_name_entry{i}"].place_info()['y'])-97)
                globals()[f"start_month_dropdown{i}"].place_configure(
                    y=int(globals()[f"start_month_dropdown{i}"].place_info()['y']) - 97)
                globals()[f"end_month_dropdown{i}"].place_configure(
                    y=int(globals()[f"end_month_dropdown{i}"].place_info()['y']) - 97)
                globals()[f"uploadList_button{i}"].place_configure(
                    y=int(globals()[f"uploadList_button{i}"].place_info()['y']) - 97)
                globals()[f"delete_workbook_buttons{i}"].place_configure(
                    y=int(globals()[f"delete_workbook_buttons{i}"].place_info()['y']) - 97)

            addNewClass_button.place_configure(x=650, y=self.mostFieldDimensionsY["addNewClass"]-97)

            class_fields.pop(button_num)
            self.noOfClasses -= 1
        else:
            self.master.switch_frame(InitializeExcelDatabases)
