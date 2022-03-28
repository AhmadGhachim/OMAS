class FileParser(object):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = list()

        self.start_time = None  # Meeting start time. Format -> 00:34:12
        self.date = None  # Meeting start date. Format -> 05/01/22


        self.leave_time = None  # Meeting leave time. Format -> 00:34:12
        self.leave_date = None  # Meeting leave date. Format -> 05/01/22

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
#####################################
    def parse_for_zooms(self):

        self.leave_time = None  # Meeting start time. Format -> 00:34:12
        self.leave_date = None  # Meeting start date. Format -> 05/01/22
        f = open(self.file_path, "r")
        try:  # copy data into python list
            for y in f:
                y = y.strip()
                y = y.split("\t")


                try:
                   # y[3] = y[3].split(", ")
                   # y[3] = {'Join Time & Date': y[3][0]}
                    #y[4] = y[4].split(", ")
                    #y[4] = {'Leave Time & Date': y[4][0]}

                    ##y[3] = {'Join Time & Date': y[3][0], 'Leave Time & Date': y[3][1]}

                 y[3] = y[3].split(", ")
                 y[3] = {'Join Date & Time': y[3][0]}

                 y[4] = y[4].split(", ")
                 y[4] = {'Leave Date & Time': y[4][0]}

                except TypeError:
                    pass
                except IndexError:
                    pass
                self.data.append(y)

        except UnicodeDecodeError:
            pass

        f.close()

        self.data = self.data[1:]  # take out header (first element) of the list

       # self.date = self.data[0][3]['Join Time & Date']
       # self.start_time = self.data[0][4]['Leave Time & Date']
        self.date = self.data[0][3]
        self.start_time = self.data[0][3]

        self.leave_time = self.data[0][4] # Meeting leave time. Format -> 00:34:12
        self.leave_date = self.data[0][4] # Meeting leave date. Format -> 05/01/22

#####################################
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
   fp0 = FileParser("/Users/josh/PycharmProjects/bugs-for-breakfast/backend/Test files/meet_file1.csv")
   fp0.parse_for_teams()
   fp0.__output__()

   fp = FileParser("/Users/josh/PycharmProjects/bugs-for-breakfast/backend/Test files/zoom_meet_file1.csv")
   fp.parse_for_zooms()
   fp.__output__()
