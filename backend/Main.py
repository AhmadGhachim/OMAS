"""This file is a placeholder for the frontend, while we are working on the integration"""

import os
import random

from WorkbookInitializer import workbook_initializer
from DataProcessor import DataProcessor

if "Excel files" not in os.listdir():
    os.mkdir("Excel files")

directory = [x[:-4] for x in os.listdir("Attendance files") if x[-4:] == ".csv"
                 and x[:-4] + ".xlsx" in os.listdir("Excel files")]

test_start_end_months = [("January", "October"), ("September", "July")]

if not len(directory):
    print("Running initializer...")
    for x in range(len(os.listdir("Class List"))):
        workbook_initializer(os.listdir("Class List")[x].split(".")[0], test_start_end_months[random.randint(0, 1)], "Class List/" + os.listdir("Class List")[x])

if len(os.listdir("Class List")) > len(os.listdir("Excel files")):
    for x in os.listdir("Class List"):
        if x[0:-4] + ".xlsx" not in os.listdir("Class List"):
            workbook_initializer(x[0:-4], test_start_end_months[1], "Class List/" + x)

directory = [x[:-4] for x in os.listdir("Attendance files") if x[-4:] == ".csv"
                 and x[:-4] + ".xlsx" in os.listdir("Excel files")]

for x in directory:
    workbook_path = "Excel files/" + x + ".xlsx"
    meeting_file_path = "Attendance files/" + x + ".csv"
    dp = DataProcessor(workbook_path, meeting_file_path, 'teams', 50, 25)
    dp.output_to_workbook()
    dp.output_to_text_file()
    dp.output_to_console()

