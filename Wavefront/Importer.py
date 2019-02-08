import logging
from .RestHelper import RestHelper

logger = logging.getLogger(__name__)


class Importer:

    def __init__(self, cluster, token):
        self.cluster = cluster
        self.token = token

    def import_data(self, data_list):
        '''
        data_list is a list which is created during processing dictionary (process_dictionary function)
            ['metric value timestamp source=mysource',
            'metric value1 timestamp1 source=mysource']

        we should concatenate all items in list with '\n' and import to wavefront.
        :param data_list:
        :return:
        '''

        if len(data_list) == 0:
            logger.info("nothing to import")
            return 0
        logger.info("importing data")
        # send part by part
        rh = RestHelper(self.cluster, token=self.token)
        if len(data_list) < 1000:
            data = "\n".join(data_list)
            c = rh.send_data_point(data)
            logger.info("data sent to Wavefront " + str(c))
            return c
        else:
            for i in range(0, len(data_list), 1000):
                data = "\n".join(data_list[i: i + 999])
                c = rh.send_data_point(data)
                logger.info("part of data sent to Wavefront " + str(c))

