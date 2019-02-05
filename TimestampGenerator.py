"""
    TimestampGenerator generates timestamp values for the given range and step
"""


class TimestampGenerator:
    def __init__(self, start, end, step):
        #todo parse to timestamps
        self.__start = start
        self.__end = end
        self.__step = step
        print("generating timestamps . . . ")

    def generate(self):
        #todo generate timestamps list and return
        timestamps = [22, 322, 5]
        return timestamps

    def get_length(self):
        return int((self.__end - self.__start) / self.__step)


