import logging
from Rest import RestCall

logger = logging.getLogger(__name__)


class RestHelper:

    def __init__(self, cluster, token):
        self.cluster = cluster
        self.token = token

    def _get_auth_header(self):
        return {"Authorization": "Bearer " + self.token}

    def get_basic_headers(self):
        headers = self._get_auth_header()
        headers.update({"Content-Type": "application/json"})
        headers.update({"Accept": "application/json"})
        return headers

    def get_url(self):
        return "http://" + self.cluster

    def check_connection(self):
        url = "https://" + self.cluster + "/api/v2/source"
        header = self._get_auth_header()
        code, result = RestCall.send_get(url, header)
        logger.info(code)
        logger.info(result)
        return code == 200

    def send_data_point(self, data):
        '''
        sending data point(s) to wavefront cluster
        we can send one or multiple data points
        data for one data point
            hello.world 1 source=myhost
        data for multiple data points
            hello.world.2 10 timestamp source=myhost
            hello.world.1 123 timestamp source=myhost
            hello.world.4 345 timestamp source=myhost1
        ****IMPORTANT****
            function doesn't check data format, make sure to send data in correct format
        :param data:
        :return:
        '''

        logger.info("sending data to WF")

        url = "https://" + self.cluster + "/report"
        headers = self._get_auth_header()
        code, result = RestCall.send_post(url, headers, data)
        logger.info(code)
        logger.info(result)
        return code == 202
