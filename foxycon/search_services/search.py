from abc import ABC
from typing import Generator

from aiohttp.log import client_logger

from foxycon import StatisticianSocNet
from foxycon.search_services.modules.algorithm_search import SearchTg
from foxycon.search_services.modules.search_soc_net import YoutubeSearch


class SearchStrategy(ABC):
    pass

class Search:
    def __init__(
        self,
        proxy=None,
        telegram_accounts=None,
        subtitles=None,
        file_settings=None,
        search_algorithm=None,
        number_age=5,
    ):
        self._file_settings = file_settings
        self._search_algorithm = search_algorithm
        self._number_age = number_age
        self._statistician_object = self.get_statistician_object(
            proxy=proxy,
            telegram_accounts=telegram_accounts,
            subtitles=subtitles,
            file_settings=file_settings,
        )

    @staticmethod
    def get_statistician_object(
        proxy, telegram_accounts, file_settings, subtitles
    ) -> StatisticianSocNet:
        return StatisticianSocNet(
            proxy=proxy,
            file_settings=file_settings,
            telegram_accounts=telegram_accounts,
            subtitles=subtitles,
        )

    @staticmethod
    def get_search_strategy(data_base_link):
        if data_base_link.analytics_obj.social_network == "youtube":
            return YoutubeSearch

    async def search(self, base_link) -> Generator:
        data_base_link = await self._statistician_object.get_data(base_link)
        search_strategy = self.get_search_strategy(data_base_link)
        generator_socnet_object = await search_strategy(
            statistician_socnet_object=self._statistician_object,
            object_statistic=data_base_link,
        ).create_generator()
        return generator_socnet_object

class TelegramSearch(SearchStrategy):
    def __init__(self, statistician_object: StatisticianSocNet):
        self.statistician_object = statistician_object

    def channel_search(self, link, text):
        pass

    async def channel_search_async(self, link, text):
        client = self.statistician_object.telegram_account_balancer.call_next()
        data = SearchTg()
        pass