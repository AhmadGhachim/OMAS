from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Frame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class InitializeExcelDatabases(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.noOfClasses = 1
        self.mostFieldDimensionsY = {
            "canvas_text": 287, 
            "entry_text": 276, 
            "start_month": 276, 
            "end_month": 276, 
            "uploadClassList": 276, 
            "addNewClass": 515,
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


        # Create new Class Upload field
        def createNewField():

            if self.noOfClasses > 2:
                addNewClass_button.place_configure(x=650, y=self.mostFieldDimensionsY["addNewClass"] + 90)
                self.mostFieldDimensionsY["addNewClass"] += 90

            globals()[f"uploadList_button_image{self.noOfClasses}"] = PhotoImage(
            file=relative_to_assets("uploadList.png"))
            globals()[f"uploadList_button{self.noOfClasses}"] = Button(
                self,
                image=globals()[f"uploadList_button_image{self.noOfClasses}"],
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_1 clicked"),
                relief="flat"
            )
            globals()[f"uploadList_button{self.noOfClasses}"].place(
                x=1092.0,
                y=self.mostFieldDimensionsY["uploadClassList"],
                width=300.0,
                height=50.0
            )

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
                foreground="#fff",
                bg="#FFFFFF",
                fg="#000000",
                insertbackground="#000000",
                highlightthickness=2,
                font=("Roboto", 24 * -1)
            )
            globals()[f"class_name_entry{self.noOfClasses}"].place(
                x=276.0,
                y=self.mostFieldDimensionsY["entry_text"],
                width=320.0,
                height=48.0
            )

            globals()[f"start_month_dropdown_image{self.noOfClasses}"] = PhotoImage(
                file=relative_to_assets("dropDown.png"))
            globals()[f"start_month_dropdown{self.noOfClasses}"] = Button(
                self,
                image=globals()[f"start_month_dropdown_image{self.noOfClasses}"],
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_4 clicked"),
                relief="flat"
            )
            globals()[f"start_month_dropdown{self.noOfClasses}"].place(
                x=628.0,
                y=self.mostFieldDimensionsY["start_month"],
                width=200.0,
                height=50.0
            )

            globals()[f"end_month_dropdown_image{self.noOfClasses}"] = PhotoImage(
                file=relative_to_assets("dropDown.png"))
            globals()[f"end_month_dropdown{self.noOfClasses}"] = Button(
                self,
                image=globals()[f"end_month_dropdown_image{self.noOfClasses}"],
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_5 clicked"),
                relief="flat"
            )
            globals()[f"end_month_dropdown{self.noOfClasses}"].place(
                x=860.0,
                y=self.mostFieldDimensionsY["start_month"],
                width=200.0,
                height=50.0
            )

            self.noOfClasses += 1
            self.mostFieldDimensionsY["canvas_text"] += 97
            self.mostFieldDimensionsY["entry_text"] += 97
            self.mostFieldDimensionsY["start_month"] += 97
            self.mostFieldDimensionsY["end_month"] += 97
            self.mostFieldDimensionsY["uploadClassList"] += 97



        #########################

        canvas.create_text(
            525.0,
            109.0,
            anchor="nw",
            text="Initialze Excel Databases",
            fill="#000000",
            font=("Inter Medium", 36 * -1)
        )


        global addNewClass_button_image
        addNewClass_button_image = PhotoImage(
            file=relative_to_assets("addNewClass.png"))
        addNewClass_button = Button(
            self,
            image=addNewClass_button_image,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_2 clicked"),
            command=createNewField,
            relief="flat"
        )
        addNewClass_button.place(
            x=650.0,
            y=515.0,
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


        global process_button_image
        process_button_image = PhotoImage(
            file=relative_to_assets("process.png"))
        process_button = Button(
            self,
            image=process_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        process_button.place(
            x=634.0,
            y=858.0,
            width=233.0,
            height=79.0
        )

        for i in range(2):
            createNewField()
