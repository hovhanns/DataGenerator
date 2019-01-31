""""@package generator
Documentation for this module.

More details.
Generates random values an
puts generated values in
various data structures
"""

import heapq
from random import randrange
from datetime import timedelta


def random_timestamp(start, end):
    """Documentation for a function.

    More details.
    Generates random timestamp
    between start and end dates
    @param start start date
    @param end end date
    @return random timestamp
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def rand_heap(start, end, num, random_function):
    """Documentation for a function.

    More details.
    Returns queue with num random values
    between start and end dates
    @param start start date
    @param end end date
    @param num size of the queue
    @param random_function generates random value
    @return queue with random values
    """
    random_values = []
    for j in range(num):
        heapq.heappush(random_values, random_function(start, end))
    return random_values
