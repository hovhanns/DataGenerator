#!/usr/bin/env python3


from DataGenerator import DataGenerator
from Config import Config

# TODO here need to add Wavefront package to pip global library and install it as a requirement
# sys.path.append("/Users/hhovhannisya/PycharmProjects/vROpsMonitoringViaWavefront")
# from Wavefront import Process

conf = Config("Config/config.json").get_config()

for metric in conf["metrics"]:
    for data in metric["data"]:
        dgen = DataGenerator(data)
        tplist = list(dgen.generate())
        metrics_dict = {metric["metric"]: tplist}
        print(metrics_dict)
# dat = Process.process_historical_data_dictionary(metrics_dict, source_name="my_source", include_tag=False)
