#!/usr/bin/env python3

from generator import timeseries

start = '2009/07/31'
end = '2009/08/31'
gen = timeseries.TimeSeriesGenerator(start, end, 'D', 10)
print("starting . . ")
for t in gen.next_point():
    print(t)
