import logging

logger = logging.getLogger(__name__)


class Process:

    @staticmethod
    def process_data_dictionary(metrics_dict, source_name):
        """
        this function will process dictionary which we passed as param.
        passed dict format is
                    {'16node_master.Analytics.threads': [(1491.0, 1538062033362), (1391.0, 1538062033352) ],
                    '16node_data1.Analytics.threads': [(1275.0, 1538062210848), (1391.0, 1538062033352)]}
            where key is metric name, value is tuple (metric_value, timestamp)
            key in dictionary should be splitted,
                16node_master.Analytics.threads should be "Analytics.threads" as metric name
                and "16node_master" as tagvalue, tagname is "node"
            hint of creating tag, node=<tagvalue>
        :param metrics_dict:
        :param source_name:
        :return:
        """
        logger.info("processing . . .")
        ret = []
        if len(metrics_dict) == 0:
            logger.info("metrics dictionary is empty")
            return ret

        data_format = "%s %s %s source=%s"
        for metric_name, values_timestamps in metrics_dict.items():
            for value_timestamp in values_timestamps:
                value, timestamp = value_timestamp
                ret.append(data_format % (metric_name, str(value), str(timestamp), source_name))
        return ret
