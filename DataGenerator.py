from DataType import DataType as dt


class DataGenerator:
    def __init__(self, start, end, type, config):
        self.__start = start
        self.__end = end
        self.__type = type
        self.__config = config

    def generate(self):
        timestamps = [445465465, 54684564, 4864684]
        values = [1, 2, 2]
        print("generated . . . ")

