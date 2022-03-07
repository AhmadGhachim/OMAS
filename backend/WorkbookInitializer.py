""" WARNING: RUNNING THIS MAY RESET ANY/ALL EXISTING WORKBOOK(S) WITH SAME NAME(S) """
import os
import sys
import openpyxl
from openpyxl.styles import Font
from timeit import default_timer

start_time = default_timer()

# classes = sys.argv[1]
# start_end_months = sys.argv[2]
# class_lists = sys.argv[3]

classes = ["CMPT 370", "MATH 211"]
start_end_months = [("January", "April"), ("September", "January")]
class_lists = ["Test files/Class List/" + x for x in os.listdir("Test files/Class List") if x[-4:] == ".txt"]

original_months = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']

months = [original_months[original_months.index(x[0]):] + original_months[:original_months.index(x[1])+1]
          if original_months.index(x[0]) > original_months.index(x[1])
          else original_months[original_months.index(x[0]):original_months.index(x[1])+1]
          for x in start_end_months]


for x, w, m in zip(classes, class_lists, months):
    class_list = open(w, 'r')
    class_list_copy = list()
    for y in class_list:
        y = y.strip()
        class_list_copy.append(y)

    wb = openpyxl.Workbook()
    wb.active.title = m[0]
    for y in m[1:]:
        wb.create_sheet(y)
    for y in wb.sheetnames:
        wb._active_sheet_index = wb.sheetnames.index(y)
        sheet = wb.active
        sheet["A1"] = "NAME"
        ft = Font(bold=True)
        sheet["A1"].font = ft
        count = 2
        for z in class_list_copy:
            sheet["A" + str(count)] = z.upper()
            count += 1
    wb._active_sheet_index = 0
    try:
        wb.save("Excel files/" + x + ".xlsx")
    except FileNotFoundError:
        os.mkdir("Excel files")
        wb.save("Excel files/" + x + ".xlsx")

print("Initialization done successfully! Time taken:", (default_timer() - start_time).__round__(4), "ms")
