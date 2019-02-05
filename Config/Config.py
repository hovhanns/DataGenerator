import json
from datetime import datetime
import re


class Config:
    def __init__(self, config_file):
        self.__config_file = config_file

        with open(self.__config_file) as f:
            self.__config = json.load(f)

        self.__config["start"] = self.__start = int(
            datetime.strptime(self.__config["start"], "%Y-%m-%d %H:%M:%S").strftime("%s") + "000")
        self.__config["end"] = self.__start = int(
            datetime.strptime(self.__config["end"], "%Y-%m-%d %H:%M:%S").strftime("%s") + "000")

        match = re.search("(\d+)([smhd])(\\b)", self.__config["step"])
        if match is not None:
            #
            d = {
                "s": 60,
                "m": 60 * 60,
                "h": 60 * 60 * 60,
                "d": 60 * 60 * 60 * 24
            }
            num = match.group(1)
            t = match.group(2)

            # step to millis
            self.__step = int(num) * d[t] * 1000
        else:
            raise ValueError("the step isn't set correctly")

    def get_config(self):
        return self.__config
