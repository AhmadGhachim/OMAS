import sys

import FileParser as Fp

path = sys.argv[1]


class DataProcessor(object):
    def __init__(self):
        self.__file_parser = Fp.FileParser(path)


def process(data):
    pass
