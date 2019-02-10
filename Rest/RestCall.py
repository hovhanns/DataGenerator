import urllib.request
import logging
import urllib
import ssl

# TODO fix this for secure connections!!!
ssl._create_default_https_context = ssl._create_unverified_context

logger = logging.getLogger(__name__)


class RestCall:

    def __init__(self):
        logger.info("fake constructor")

    @staticmethod
    def send_get(url, headers):
        logger.info("sending get request")
        method = "GET"
        handler = urllib.request.HTTPHandler()
        opener = urllib.request.build_opener(handler)
        try:
            request = urllib.request.Request(url)
        except ValueError as e:
            logger.error(e)
            return None, None

        for key, value in headers.items():
            request.add_header(key, value)

        request.get_method = lambda: method
        try:
            connection = opener.open(request)
        except urllib.request.HTTPError as e:
            logger.error(e)
            return None, None
        except KeyboardInterrupt:
            logger.error("Keyboard interrupt")
        except Exception as e:
            logger.error("unknown exception is occured", e)
            return None, None
        response = connection.read()
        return connection.code, response

    @staticmethod
    def send_post(url, headers, body):
        logger.info("sending post request")
        logger.info(url)
        logger.info(headers)
        #logger.info(body)
        method = "POST"
        handler = urllib.request.HTTPHandler()
        opener = urllib.request.build_opener(handler)
        data = body.encode('utf-8')

        try:
            request = urllib.request.Request(url, data=data)
        except ValueError as e:
            logger.error(e)
            return None, None

        for key, value in headers.items():
            request.add_header(key, value)
        request.get_method = lambda: method
        try:
            connection = opener.open(request)
        except urllib.request.HTTPError as e:
            logger.error(e)
            return None, None
        except KeyboardInterrupt:
            logger.error("Keyboard interrupt")
        except Exception as e:
            logger.error("unknown exception is occured", e)
            return None, None

        response = connection.read()
        return connection.code, response

    @staticmethod
    def send_delete(url, headers):
        logger.info("sending post request")
        logger.info(url)
        logger.info(headers)

        method = "DELETE"
        handler = urllib.request.HTTPHandler()
        opener = urllib.request.build_opener(handler)

        try:
            request = urllib.request.Request(url)
        except ValueError as e:
            logger.error(e)
            return None, None

        for key, value in headers.items():
            request.add_header(key, value)
        request.get_method = lambda: method
        try:
            connection = opener.open(request)
        except urllib.request.HTTPError as e:
            logger.error(e)
            return None, None
        except KeyboardInterrupt:
            logger.error("Keyboard interrupt")
        except Exception as e:
            logger.error("unknown exception is occured", e)
            return None, None

        response = connection.read()
        return connection.code, response
