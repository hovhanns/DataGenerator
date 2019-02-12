""""@package generator
Documentation for this module.

More details.
Generates time series
"""

import pandas as pd
import numpy as np
import math
from generator import random as randgen


class TimeSeriesGenerator:
    def __init__(self, start, end, freq, noise):
        self.__start = pd.to_datetime(start)
        self.__end = pd.to_datetime(end)
        self.__freq = freq

        # counting number of total points
        self.__totalPointsCount = math.ceil((self.__end - self.__start)/np.timedelta64(1, freq))

        # generating random points
        random_points_count = math.floor((self.__totalPointsCount * noise) / 100)
        self.__random_time_series = randgen.rand_list(self.__start, self.__end, random_points_count, randgen.random_timestamp)

    def next_point(self):
        time_series = self.__start
        random_time_series_iter = iter(self.__random_time_series)
        random_time_series = next(random_time_series_iter, None)
        yield time_series
        while time_series < self.__end:
            time_series = time_series + np.timedelta64(1, self.__freq)
            if random_time_series is None or (random_time_series is not None and time_series < random_time_series):
                yield time_series
            else:
                yield random_time_series
                random_time_series = next(random_time_series_iter, None)

    def get_all_data(self):
        time_series_idx = pd.date_range(self.__start, self.__end, freq=self.__freq)
        random_time_series_iter = iter(self.__random_time_series)
        random_time_series = next(random_time_series_iter, None)
        all_data = []
        if random_time_series is None:
            return time_series_idx
        for time_series in time_series_idx:
            if random_time_series is None or (random_time_series is not None and time_series < random_time_series):
                all_data.append(time_series)
            else:
                all_data.append(random_time_series)
                random_time_series = next(random_time_series_iter, None)
        return all_data

