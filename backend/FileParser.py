class FileParser(object):
    def __init__(self, path: str):
        self.file_path = path  # path to the .csv file
        self.data = list()
        self.start_time = None  # Meeting start time. Format -> 00:34:12
        self.date = None  # Meeting start date. Format -> 05/01/22

    def parse_for_teams(self):
        """
        Parses data from the given meeting report file and stores it in 'data'
        :return: None
        """
        f = open(self.file_path, "r")
        try:  # copy data into python list
            for y in f:
                y = y.strip()
                y = y.split("\t")
                y[0] = y[0].upper()
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
        self.data = self.data[1:]

    # To be implemented
    def parse_for_zoom(self):
        pass

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
    fp = FileParser("/Users/xecute/Desktop/370Repo/backend/Test files/test.csv")
    fp.parse_for_teams()
    fp.__output__()
