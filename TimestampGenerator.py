"""
    TimestampGenerator generates timestamp values for the given range and step
"""


class TimestampGenerator:
    def __init__(self, start, end, step):
        self.__start = start
        self.__end = end
        self.__step = step
        print("generating timestamps . . . ")

    def generate(self):
        #todo generate timestamps list and return
        timestamps = []
        for i in range(self.__start, self.__end, self.__step):
            timestamps.append(i)
        return timestamps

    def get_length(self):
        return int((self.__end - self.__start) / self.__step)


