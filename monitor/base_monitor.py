from abc import ABCMeta, abstractmethod
from time import sleep
from typing import Callable

from logger import get_logger

logger = get_logger(__name__)


class Monitor(metaclass=ABCMeta):
    """
    Абстрактный класс для мониторинга состояния блокчейна.
    """

    def __init__(self, hard_fork_time_stamp: int, on_hard_fork: Callable,
                 host: str = '127.0.0.1', port: str = '18332', user: str = 'user', password: str = 'password'):
        self.service_url = f'http://{user}:{password}@{host}:{port}'
        self.user = user
        self.password = password
        self.hard_fork_time_stamp = hard_fork_time_stamp
        self.on_hard_fork = on_hard_fork

    @abstractmethod
    def get_median_time(self) -> int:
        """Достает информацию о медианном времени последних 11 блоков."""

    def start(self):
        """
        Запускает монитор.
        """
        while True:
            median_time = self.get_median_time()
            if median_time >= self.hard_fork_time_stamp:
                self.on_hard_fork(median_time)
                break
            minutes_left = (self.hard_fork_time_stamp - median_time) // 60
            logger.info(f'current median time {median_time}; about {minutes_left} +- 10 min minutes left')
            sleep(5)
