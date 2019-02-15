#!/usr/bin/env python3

import logging.config
import yaml

from DataGenerator import DataGenerator
from Config import Config

from Wavefront import Process
from Wavefront import Importer

logging.config.dictConfig(yaml.load((open('logging.yaml', 'r'))))
logger = logging.getLogger(__name__)

conf = Config("Config/config.json").get_config()
imp = Importer(conf["wavefront"]["cluster"], conf["wavefront"]["token"])

for metric in conf["metrics"]:
    for data in metric["data"]:
        dgen = DataGenerator(data)
        tplist = list(dgen.generate())
        metrics_dict = {metric["metric"]: tplist}
        processed = Process.process_data_dictionary(metrics_dict, metric["source"])
        #print(processed)
        logger.info(imp.import_data(processed))
        #print(metrics_dict)

        logger.debug(metrics_dict)

# dat = Process.process_historical_data_dictionary(metrics_dict, source_name="my_source", include_tag=False)
