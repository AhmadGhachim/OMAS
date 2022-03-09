import sys
from difflib import SequenceMatcher
import openpyxl
import MathFunctions
import FileParser as Fp
import ExcelFunctions
import WorkbookInitializer

path = sys.argv[1]


class DataProcessor(object):
    def __init__(self):
        self.__file_parser = Fp.FileParser(path)
        self.__processed_data = None
        self.__excel_file = None

    def call_processor(self, data: list, meeting_service: str, file_path: str):
        if meeting_service == 'Zoom':
            self.__processed_data = self.__file_parser.parse_for_teams()

    def process(self, data: list, file_path: str):
        student_record = dict()
        for y in data:
            try:
                student_record[y[0].upper()] += MathFunctions.duration(y[1][-8:], y[2][-8:])
            except KeyError:
                student_record[y[0].upper()] = MathFunctions.duration(y[1][-8:], y[2][-8:])

        wb = openpyxl.load_workbook(file_path)  # Open class workbook

        names = list()  # List to store student names
        sheet = wb.active

        # Write date on top of the column where data is to be stored
        sheet[ExcelFunctions.row_col_2_cell(1, int(self.__file_parser.date.split("/")[0]) + 1)] = \
            WorkbookInitializer.original_months[int(self.__file_parser.date.split("/")[1]) - 1][:3] + " " + \
            self.__file_parser.date.split("/")[0]

        # Create a list of student names ('names') from the workbook
        row_count = 2
        cell_data = sheet.cell(row_count, 1).value
        while cell_data is not None:
            names.append(cell_data)
            row_count += 1
            cell_data = sheet.cell(row_count, 1).value

        # Check if all names are correctly entered
        exceptions = list()
        exceptions_replacement = list()

        i = 0
        for y in [z[0] for z in data]:
            if y in names:
                pass
            else:
                exceptions.append(y)
                similarity, index = 0, 0
                count = 0
                for z in names:
                    match = SequenceMatcher(a=y, b=z).ratio()
                    if match > similarity:
                        similarity = match
                        index = count
                    count += 1
                data[i][0] = names[index]
                exceptions_replacement.append(names[index])
            i += 1

