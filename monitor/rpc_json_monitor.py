import json

import requests
from requests import HTTPError
from requests.auth import HTTPBasicAuth

from monitor.base_monitor import Monitor
from monitor.exceptions import MonitoringException


class RPCJSONMonitor(Monitor):
    """
    Использует Bitcoin RPC-JSON interface, чтобы достать мидианное время.
    """

    def get_median_time(self) -> int:
        try:
            headers = {
                'content-type': 'application/json'
            }
            payload = {
                'method': 'getblockchaininfo',
                'jsonrpc': '2.0',
                'params': [],
                'id': 'jsonrpc',
            }
            basic_auth = HTTPBasicAuth(self.user, self.password)
            response = requests.post(self.service_url, headers=headers, auth=basic_auth, data=json.dumps(payload))
            response.raise_for_status()
            response_json = response.json()
            error = response_json.get('error', None)
            if error is not None:
                raise MonitoringException(error)
            median_time = int(response_json['result']['mediantime'])
            return median_time
        except HTTPError as e:
            raise MonitoringException(e)
