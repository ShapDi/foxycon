import inspect

from typing import Callable

from foxycon.utils.clients_handler import ClientsHandler
from foxycon.utils.call_balancer import CallBalancer
from foxycon.analysis_services.сontent_analyzer import ContentAnalyzer
from foxycon.statistics_services.modules.statistics_social_network import (
    StatisticianModuleStrategy,
)


class StatisticianSocNet:
    statistics_modules = {
        subclass().__str__(): subclass
        for subclass in StatisticianModuleStrategy.__subclasses__()
    }
    # clients_handlers = {
    #     subclass().__str__(): subclass() for subclass in ClientsHandler.__subclasses__()
    # }

    def __init__(
        self, proxy=None, file_settings=None, clients_handlers=None, subtitles=None
    ):
        self._proxy = proxy
        self._clients_handlers = clients_handlers

        # (
        #     clients_handlers if clients_handlers is not None else self.clients_handlers
        # )
        self._subtitles = subtitles
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

    async def get_data(self, link):
        if self._proxy_balancer is not None:
            self._proxy = self._proxy_balancer.call_next()

        data = self.get_basic_data(link)

        class_statistics = self.statistics_modules.get(f"{data.social_network}")
        if self.is_coroutine(class_statistics().get_data):
            data = await class_statistics(proxy=self._proxy).get_data(
                data, clients_handlers=self._clients_handlers
            )

        else:
            data = class_statistics(
                proxy=self._proxy, subtitles=self._subtitles
            ).get_data(data)
        return data
