import os

from backend.MathFunctions import am_pm_to_24_hours

path = os.path.abspath(os.path.pardir)
path = path.replace("\\", "/", path.count("\\"))

class FileParser(object):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = list()

        self.start_time = None  # Meeting start time. Format -> 00:34:12
        self.date = None  # Meeting start date. Format -> 05/01/22

        self.leave_time = None  # Meeting leave time. Format -> 00:34:12

    def parse_for_teams(self):
        f = open(self.file_path, "r")
        try:  # copy data into python list
            for y in f:
                y = y.strip()
                y = y.split("\t")

                try:
                    y[2] = y[2].split(", ")
                    y[2] = {'date': y[2][0], 'time': y[2][1]}
                except TypeError:
                    pass
                except IndexError:
                    pass
                self.data.append(y)

        except UnicodeDecodeError:
            pass

        f.close()

        self.data = self.data[1:]  # take out header (first element) of the list

        self.date = self.data[0][2]['date']
        self.start_time = self.data[0][2]['time']

    def parse_for_zoom(self):

      #  self.leave_time = None  # Meeting start time. Format -> 00:34:12
      #  self.leave_date = None  # Meeting start date. Format -> 05/01/22
        f = open(self.file_path, "r")
        data = list()
        # copy data into python list
        for y in f:
            y = y.strip()
            y = y.split("\t")
            data.append(y)

        data = data[1:]

        for y in data:
            y[3] = y[3].split(" ")
            join = dict()
            join["date"] = y[3][0]
            join["time"] = am_pm_to_24_hours(" ".join(y[3][1:]))

            y[4] = y[4].split(" ")
            leave = dict()
            leave["date"] = y[4][0]
            leave["time"] = am_pm_to_24_hours(" ".join(y[4][1:]))

            self.data.append([y[0], "Joined", join.copy()].copy())
            self.data.append([y[0], "Left", leave.copy()].copy())


        f.close()

        self.date = self.data[0][2]['date']

        self.start_time = self.data[0][2]['time']
        self.leave_time = self.data[1][2]['time']

        self.data = self.data[2:]

    def parse_for_webex(self):
        pass

    def __str__(self):
        string = ''
        for x in self.data:
            string += str(x) + "\n"
        return string[0:-1]

    def __output__(self):
        for x in self.data:
            for z in x:
                print(str(z) + "  " * 6, end='')
            print()


if __name__ == '__main__':
   fp0 = FileParser(path + "/backend/Test files/zoom_meet_file1.csv")
   fp0.parse_for_zoom()
   fp0.__output__()

   fp = FileParser(path + "/backend/Test files/zoom_meet_file2.csv")
   fp.parse_for_zoom()
   fp.__output__()

   fp1 = FileParser(path + "/backend/Attendance files/CMPT 370.csv")
   fp1.parse_for_teams()
   fp1.__output__()