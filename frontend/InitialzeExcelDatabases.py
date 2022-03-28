from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Frame, StringVar, OptionMenu
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import sys

sys.path.append("../backend")

from backend.WorkbookInitializer import workbook_initializer

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


month_Options= ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class InitializeExcelDatabases(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.noOfClasses = 0
        self.mostFieldDimensionsY = {
            "canvas_text": 287, 
            "entry_text": 276, 
            "start_month": 276, 
            "end_month": 276, 
            "uploadClassList": 276, 
            "addNewClass": 400,
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

        self.createNewField(canvas)

        canvas.create_text(
            525.0,
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
            x=650.0,
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
            x=109.0,
            y=89.0,
            width=125.0,
            height=50.0
        )


        # initialize workbook
        def initializeWorkbookDatabase():

            for i in range(self.noOfClasses):
                if None in [globals()[f"filename{i+1}"], globals()[f"class_name_entry{i+1}"].get()] or globals()[f"start_month{i+1}"].get() not in month_Options or globals()[f"end_month{i+1}"].get() not in month_Options:
                    messagebox.showerror(title="warning", message="You are required to fill out every field")
                    return
                
                workbook_initializer(globals()[f"class_name_entry{i+1}"].get(), (globals()[f"start_month{i+1}"].get(), globals()[f"end_month{i+1}"].get()), globals()[f"filename{i+1}"])

                globals()[f"class_name_entry{i+1}"].delete(0, END)
                globals()[f"start_month{i+1}"].set("Select class start period")
                globals()[f"end_month{i+1}"].set("Select class end period")
                globals()[f"filename{i+1}"] = None
                globals()[f"uploadList_button{i+1}"].configure(text="+  Upload Student Name List")

            messagebox.showinfo(title="success", message="Workbook successfully created")

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
            x=634.0,
            y=800.0,
            width=233.0,
            height=79.0
        )


    def createNewField(self, canvas):
            if self.noOfClasses > 0 and ( None in [globals()[f"filename{self.noOfClasses}"], globals()[f"class_name_entry{self.noOfClasses}"]] or globals()[f"start_month{self.noOfClasses}"].get() not in month_Options or globals()[f"end_month{self.noOfClasses}"].get() not in month_Options):
                messagebox.showerror(title="warning", message="You cannot add another field while current one has not been filled completely")
                return

            if self.noOfClasses >= 1:
                addNewClass_button.place_configure(x=650, y=self.mostFieldDimensionsY["addNewClass"] + 90)
                self.mostFieldDimensionsY["addNewClass"] += 90

            self.noOfClasses += 1

            if self.noOfClasses == 5:
                addNewClass_button.place_forget()

            # to upload class list
            def UploadAction():
                globals()[f"filename{self.noOfClasses}"] = filedialog.askopenfilename()
                if globals()[f"filename{self.noOfClasses}"] and globals()[f"uploadList_button{self.noOfClasses}"]:
                    print('Selected:', globals()[f"filename{self.noOfClasses}"])
                    globals()[f"uploadList_button{self.noOfClasses}"].configure(text=globals()[f"filename{self.noOfClasses}"].split("/")[-1])
            #####################################################


            globals()[f"uploadList_button{self.noOfClasses}"] = Button(
                self,
                text="+  Upload Student Name List",
                borderwidth=0,
                highlightthickness=0,
                font=("Roboto", 20 * -1),
                command=UploadAction,
                relief="flat",
                bg="#fff"
            )
            globals()[f"uploadList_button{self.noOfClasses}"].place(
                x=1092.0,
                y=self.mostFieldDimensionsY["uploadClassList"],
                width=300.0,
                height=50.0
            )
            globals()[f"filename{self.noOfClasses}"] = None # associate a file path with a new row of fields


            canvas.create_text(
            109.0,
            self.mostFieldDimensionsY["canvas_text"],
            anchor="nw",
            text="Class " + str(self.noOfClasses),
            fill="#000000",
            font=("Roboto", 28 * -1)
            )

            globals()[f"class_name_entry{self.noOfClasses}"] = Entry(
                self,
                bd=0,
                bg="#FFFFFF",
                fg="#000000",
                insertbackground="#000000",
                highlightcolor="#fff",
                highlightthickness=2,
                font=("Roboto", 20 * -1)
            )
            globals()[f"class_name_entry{self.noOfClasses}"].place(
                x=276.0,
                y=self.mostFieldDimensionsY["entry_text"],
                width=320.0,
                height=48.0
            )


            globals()[f"start_month{self.noOfClasses}"] = StringVar(self)
            globals()[f"end_month{self.noOfClasses}"] = StringVar(self)
            globals()[f"start_month{self.noOfClasses}"].set("Select class start period")
            globals()[f"end_month{self.noOfClasses}"].set("Select class end period")


            globals()[f"start_month_dropdown{self.noOfClasses}"] = OptionMenu(
                self,
                globals()[f"start_month{self.noOfClasses}"],
                *month_Options,
                # command=lambda: print("button_4 clicked"),
            )
            globals()[f"start_month_dropdown{self.noOfClasses}"].place(
                x=628.0,
                y=self.mostFieldDimensionsY["start_month"],
                width=200.0,
                height=50.0
            )

        
            globals()[f"end_month_dropdown{self.noOfClasses}"] = OptionMenu(
                self,
                globals()[f"end_month{self.noOfClasses}"],
                *month_Options,
                # command=lambda: print("button_4 clicked"),
            )
            globals()[f"end_month_dropdown{self.noOfClasses}"].place(
                x=860.0,
                y=self.mostFieldDimensionsY["start_month"],
                width=200.0,
                height=50.0
            )

            self.mostFieldDimensionsY["canvas_text"] += 97
            self.mostFieldDimensionsY["entry_text"] += 97
            self.mostFieldDimensionsY["start_month"] += 97
            self.mostFieldDimensionsY["end_month"] += 97
            self.mostFieldDimensionsY["uploadClassList"] += 97