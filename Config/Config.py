import json
from datetime import datetime
import re


class Config:
    def __init__(self, config_file):
        self.__config_file = config_file

        with open(self.__config_file) as f:
            self.__config = json.load(f)

        self.__config["start"] = Config.__parse_date_to_millis(self.__config["start"])
        self.__config["end"] = Config.__parse_date_to_millis(self.__config["end"])
        self.__config["step"] = Config.__parse_step_to_millis(self.__config["step"])

    def get_config(self):
        return self.__config

    @staticmethod
    def __parse_date_to_millis(date):
        return int(datetime.strptime(date, "%Y-%m-%d %H:%M:%S").strftime("%s") + "000")

    @staticmethod
    def __parse_step_to_millis(step):
        match = re.search("(\d+)([smhd])(\\b)", step)
        if match is not None:
            #
            d = {
                "s": 1,
                "m": 60,
                "h": 60 * 60,
                "d": 60 * 60 * 24
            }
            num = match.group(1)
            t = match.group(2)

            # step to millis
            return int(num) * d[t] * 1000
        else:
            raise ValueError("the step isn't set correctly")
