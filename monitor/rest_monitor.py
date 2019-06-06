import requests
from requests import HTTPError

from monitor.base_monitor import Monitor
from monitor.exceptions import MonitoringException


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
            return median_time
        except HTTPError as e:
            raise MonitoringException(e)
