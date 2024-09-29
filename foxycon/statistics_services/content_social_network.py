import inspect
import asyncio

from typing import Callable

from foxycon.utils.call_balancer import CallBalancer
from foxycon.analysis_services.сontent_analyzer import ContentAnalyzer
from foxycon.statistics_services.modules.statistics_social_network import StatisticianModuleStrategy


class StatisticianSocNet:
    statistics_modules = {subclass().__str__(): subclass for subclass in StatisticianModuleStrategy.__subclasses__()}

    def __init__(self, proxy=None, file_settings=None, telegram_accounts=None):
        self._proxy = proxy
        self._telegram_accounts = telegram_accounts
        self._file_settings = file_settings

        if self._proxy is not None:
            self._proxy_balancer = CallBalancer(self._proxy)
        else:
            self._proxy_balancer = None

    @staticmethod
    def is_coroutine(func: Callable):
        return inspect.iscoroutinefunction(func)

    @staticmethod
    def get_basic_data(link: str):
        data = ContentAnalyzer().get_data(link)
        return data

    def get_data(self, link):

        if self._proxy_balancer is not None:
            self._proxy = self._proxy_balancer.call_next()

        data = self.get_basic_data(link)

        class_statistics = self.statistics_modules.get(f"{data.social_network}")
        if self.is_coroutine(class_statistics().get_data):
            data = asyncio.run(class_statistics().get_data(data))
        else:
            data = class_statistics(proxy=self._proxy).get_data(data)
        return data
