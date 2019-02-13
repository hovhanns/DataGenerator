from TimestampGenerator import TimestampGenerator
from ValueGenerator import ValueGenerator


class DataGenerator:
    def __init__(self, config):
        self.__config = config

    def generate(self):
        tgen = TimestampGenerator(self.__config["start"], self.__config["end"], self.__config["step"])
        timestamps = tgen.generate()

        vgen = ValueGenerator(self.__config["type"], len(timestamps), self.__config["parameters"])
        values = vgen.generate()
        return zip(values, timestamps)
