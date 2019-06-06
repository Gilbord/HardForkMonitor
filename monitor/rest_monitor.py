import requests
from requests import HTTPError

from logger import get_logger
from monitor.base_monitor import Monitor
from monitor.exceptions import MonitoringException

logger = get_logger(__name__)


class RestMonitor(Monitor):
    """
    Использует Bitcoin rest interface, чтобы достать мидианное время.
    """

    def get_median_time(self) -> int:
        try:
            response = requests.get(f'{self.service_url}/rest/chaininfo.json')
            response.raise_for_status()
            median_time = int(
                response.json()['mediantime']
            )
            logger.info(f'current median time {median_time}')
            return median_time
        except HTTPError as e:
            raise MonitoringException(e)
