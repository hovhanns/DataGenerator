import logging
from .RestHelper import RestHelper
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

logger = logging.getLogger(__name__)


class Importer:

    def __init__(self, cluster, token):
        self.cluster = cluster
        self.token = token
        self.chunk_size = 1000
        self.thread_count = 100

    # TODO: remove this function where import_data_multi_thread works fine
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

    def import_data_multi_thread(self, data_list):
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
        import_res = False
        if len(data_list) < self.chunk_size:
            import_res = self.__import(data_list, "data sent to Wavefront ")
        else:
            msg = "data from %d to %d sent to Wavefront "
            tasks = [(data_list[i: i + self.chunk_size - 1], msg % (i, (i + self.chunk_size - 1)))
                     for i in range(0, len(data_list), self.chunk_size)]

            with ThreadPoolExecutor(max_workers=self.thread_count) as executor:
                results = executor.map(lambda p: self.__import(*p), tasks)

            for result in results:
                import_res = import_res and result

        return import_res

    def __import(self, data_list, message):
        rh = RestHelper(self.cluster, token=self.token)
        data = "\n".join(data_list)
        c = rh.send_data_point(data)
        logger.info(message + str(c))
        return c

