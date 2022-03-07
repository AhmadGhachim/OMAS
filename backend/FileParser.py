class FileParser(object):
    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__data = list()

        self.__start_time = None  # Time of first join of user
        self.__date = None  # Date of first join of user

    def parse_for_teams(self):
        f = open(self.__file_path, "r")
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
                self.__data.append(y)

        except UnicodeDecodeError:
            pass

        f.close()

        self.__data = self.__data[1:]  # take out header aka first element of a list

        self.__date = self.__data[0][2]['date']
        self.__start_time = self.__data[0][2]['time']

    def __output__(self):
        for x in self.__data:
            for z in x:
                print(str(z) + "  " * 6, end='')
            print()


if __name__ == '__main__':
    fp = FileParser("/Users/josh/PycharmProjects/bforb/backend/Test files/test.csv")
    fp.parse_for_teams()
    fp.__output__()

