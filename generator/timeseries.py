""""@package generator
Documentation for this module.

More details.
Generates time series
"""

import pandas as pd
import numpy as np
import heapq
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
        random_points_count = math.ceil((self.__totalPointsCount * noise) / 100)
        self.__random_points = randgen.rand_heap(self.__start, self.__end, random_points_count, randgen.random_timestamp)

    # TODO refactor me :)
    def next_point(self):
        time_series = self.__start
        random_time_series = None
        if len(self.__random_points) != 0:
            random_time_series = heapq.heappop(self.__random_points)
        yield time_series
        while time_series < self.__end:
            time_series = time_series + np.timedelta64(1, self.__freq)
            if random_time_series is None or (random_time_series is not None and time_series < random_time_series):
                yield time_series
            else:
                yield random_time_series
                if len(self.__random_points) != 0:
                    random_time_series = heapq.heappop(self.__random_points)
                else:
                    random_time_series = None

