import inspect

from typing import Callable, Type, Union

from foxycon.analysis_services.сontent_analyzer import ContentAnalyzer
from foxycon.data_structures.analysis_type import ResultAnalytics
from foxycon.data_structures.statistician_type import (
    YouTubeContentData,
    YouTubeChannelsData,
    TelegramPostData,
    TelegramChatData,
    InstagramContentData,
)
from foxycon.statistics_services.modules.statistics_social_network import (
    StatisticianModuleStrategy,
)
from .modules.statistics_telegram import TelegramGroup
from .modules.statistics_youtube import YouTubeChannel, YouTubeContent
from foxycon.utils.balancers import TelegramBalancer, ProxyBalancer
from .statistics_exceptions import RequiredTelegramAccount


class StatisticianSocNet:
    def __init__(
        self, proxy=None, file_settings=None, telegram_account=None, subtitles=None
    ):
        self._proxy = proxy
        self._telegram_account = telegram_account

        self._subtitles = subtitles
        self._file_settings = file_settings

        if self._proxy is not None:
            self._proxy_balancer = ProxyBalancer(self._proxy)
        else:
            self._proxy_balancer = None

        if self._telegram_account is not None:
            self._telegram_account_balancer = TelegramBalancer(self._telegram_account)
        else:
            self._telegram_account_balancer = None

    @staticmethod
    def is_coroutine(func: Callable):
        return inspect.iscoroutinefunction(func)

    @staticmethod
    def get_basic_data(link: str):
        data = ContentAnalyzer().get_data(link)
        return data

    # @staticmethod
    # def get_statistician_module_strategy(
    #     social_network: str,
    # ) -> Type[StatisticianModuleStrategy] | None:
    #     match social_network:
    #         case "youtube":
    #             return YouTubeStatistician
    #         case "instagram":
    #             return InstagramStatistician
    #         case "telegram":
    #             return TelegramStatistician
    #     return None

    def get_statistician_module_strategy(
        self,
        social_network: ResultAnalytics,
    ) -> Type[StatisticianModuleStrategy] | None:
        match (social_network.social_network, social_network.content_type):
            case ("youtube", "video"):
                return YouTubeContent
            case ("youtube", "channel"):
                return YouTubeChannel
            case ("telegram", "channel"):
                if self._telegram_account is None:
                    raise RequiredTelegramAccount()
                return TelegramGroup
        return None

    async def get_data_async(
        self, link
    ) -> Union[
        YouTubeContentData,
        YouTubeChannelsData,
        InstagramContentData,
        TelegramPostData,
        TelegramChatData,
    ]:
        if self._proxy_balancer is not None:
            self._proxy = self._proxy_balancer.call_next()

        if self._telegram_account_balancer is not None:
            await self._telegram_account_balancer.init_call_async()
            self._telegram_account = self._telegram_account_balancer.call_next()

        link_analytics = self.get_basic_data(link)
        class_statistics = self.get_statistician_module_strategy(link_analytics)

        data = await class_statistics(proxy=self._proxy).get_data_async(
            link_analytics, clients_handlers=self._telegram_account
        )
        return data

    def get_data(
        self, link
    ) -> Union[
        YouTubeContentData,
        YouTubeChannelsData,
        InstagramContentData,
        TelegramPostData,
        TelegramChatData,
    ]:
        if self._proxy_balancer is not None:
            self._proxy = self._proxy_balancer.call_next()

        if self._telegram_account_balancer is not None:
            self._telegram_account_balancer.init_call()
            self._telegram_account = self._telegram_account_balancer.call_next()

        link_analytics = self.get_basic_data(link)

        class_statistics = self.get_statistician_module_strategy(link_analytics)

        data = class_statistics(proxy=self._proxy, subtitles=self._subtitles).get_data(
            link_analytics, clients_handlers=self._telegram_account
        )

        return data
