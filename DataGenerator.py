from DataType import DataType as dt
from TimestampGenerator import TimestampGenerator

class DataGenerator:
    def __init__(self, config):
        self.__config = config

    def generate(self):
        tgen = TimestampGenerator(self.__config["start"],self.__config["stop"], self.__config["step"])
        timestamps = tgen.generate()
        values = list(timestamps)
        print("generated . . . ")

