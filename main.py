#!/usr/bin/env python3


from DataGenerator import DataGenerator
from Config import Config

conf = Config("Config/config.json").get_config()

dgen = DataGenerator(conf)
tplist = list(dgen.generate())
print(len(tplist))
for t in tplist:
    print(t)
