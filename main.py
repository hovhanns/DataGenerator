#!/usr/bin/env python3


from DataGenerator import DataGenerator
from Config import Config

# TODO here need to add Wavefront package to pip global library and install it as a requirement
# sys.path.append("/Users/hhovhannisya/PycharmProjects/vROpsMonitoringViaWavefront")
from Wavefront import Process
from Wavefront import Importer

conf = Config("Config/config.json").get_config()
imp = Importer(conf["wavefront"]["cluster"], conf["wavefront"]["token"])

for metric in conf["metrics"]:
    for data in metric["data"]:
        dgen = DataGenerator(data)
        tplist = list(dgen.generate())
        metrics_dict = {metric["metric"]: tplist}
        processed = Process.process_data_dictionary(metrics_dict, metric["source"])
        #print(processed)
        print(imp.import_data(processed))
        #print(metrics_dict)

        print(metrics_dict)

# dat = Process.process_historical_data_dictionary(metrics_dict, source_name="my_source", include_tag=False)
