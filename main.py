import argparse

from logger import get_logger
from monitor import RestMonitor, RPCJSONMonitor, MonitoringException

logger = get_logger(__name__)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Monitor hard fork.')
    parser.add_argument('--timestamp', metavar='timestamp', type=int,
                        help='an integer for the hard fork timestamp')
    parser.add_argument('--user', default='user',
                        help='username to get access to node')
    parser.add_argument('--password', default='user',
                        help='password to get access to node')
    parser.add_argument('--host', default='127.0.0.1',
                        help='Node\' s host')
    parser.add_argument('--port', default='18332',
                        help='Node\' s host')
    parser.add_argument('--mode', default='rest', choices=['rpc', 'rest'],
                        help='Node\' s running mode. [If bitcoind run with -rest key then use -rest key. If bitcoind '
                             'run with -server key then use -rpc]')
    args = parser.parse_args()

    monitor_args = {
        'hard_fork_time_stamp': args.timestamp,
        'on_hard_fork': lambda timestamp: logger.info(f'hard fork {timestamp}'),
        'host': args.host,
        'port': args.port,
        'user': args.user,
        'password': args.password
    }

    if args.mode == 'rpc':
        monitor = RPCJSONMonitor(**monitor_args)
    else:
        monitor = RestMonitor(**monitor_args)
    try:
        monitor.start()
    except MonitoringException as e:
        logger.error(e)
