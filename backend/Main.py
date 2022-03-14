"""This file is a placeholder for the frontend, while we are working on the integration"""

import os

from backend.DataProcessor import DataProcessor

directory = [x[:-4] for x in os.listdir("Attendance files") if x[-4:] == ".csv"
                 and x[:-4] + ".xlsx" in os.listdir("Excel files")]

if not len(directory):
    print("Running initializer...")
    for x in os.listdir("Class List"):
        pass

for x in directory:
    workbook_path = "Excel files/" + x + ".xlsx"
    meeting_file_path = "Attendance files/" + x + ".csv"
    DataProcessor(x, workbook_path, meeting_file_path, 50, 25)

