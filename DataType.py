from enum import Enum


"""This class is for storing all data types"""


class DataType(Enum):
    CONSTANT = 1
    NEAR_CONSTANT = 2
    TRENDY = 3
    NEAR_TRENDY = 4
    STATIONARY = 5
    TREND_STATIONARY = 6
    UNIT_ROOT = 7

