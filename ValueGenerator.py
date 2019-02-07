"""
    ValueGenerator generates values by given type and config
"""
from generator import Core
from DataType import DataType


class ValueGenerator:
    type_functions = {
        DataType.CONSTANT: Core.const,
        DataType.NEAR_CONSTANT: Core.near_constant,
        DataType.TRENDY: Core.trendy,
        DataType.NEAR_TRENDY: Core.near_trendy,
        DataType.STATIONARY: Core.stationary,
        DataType.TREND_STATIONARY: Core.trend_stationary,
        DataType.UNIT_ROOT: "here should be unit root function"
    }

    def __init__(self, type, size):
        self.__type = type
        self.__size = size
        print("generating values . . . ")

    def generate(self):
        values = ValueGenerator.type_functions[DataType[self.__type]](size=self.__size)
        return values
