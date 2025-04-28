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
from foxycon.utils.balancers import TelegramBalancer, ProxyBalancer, InstagramBalancer
from .statistics_exceptions import RequiredTelegramAccount
from ..data_structures.balancer_type import Proxy, TelegramAccount, InstagramAccount
from ..utils.storage_manager import StorageManager


class StatisticianSocNet:
    def __init__(
        self,
        proxy: list[Proxy] | None = None,
        telegram_account: list[TelegramAccount] = None,
        instagram_account: list[InstagramAccount] = None,
        file_storage: str | None = None,
    ):
        self._proxy = proxy
        self._instagram_account = instagram_account
        self._telegram_account = telegram_account
        self._file_storage = file_storage

        if proxy is not None:
            self._proxy_balancer = ProxyBalancer(proxy)

        if instagram_account is not None:
            self._instagram_balancer = InstagramBalancer(instagram_account)

        if telegram_account is not None:
            self._telegram_balancer = TelegramBalancer(telegram_account)

        if file_storage is not None:
            storage = StorageManager(file_storage)

    async def get_data_async(
        self, link
    ) -> Union[
        YouTubeContentData,
        YouTubeChannelsData,
        InstagramContentData,
        TelegramPostData,
        TelegramChatData,
    ]:
        pass

    def get_data(
        self, link
    ) -> Union[
        YouTubeContentData,
        YouTubeChannelsData,
        InstagramContentData,
        TelegramPostData,
        TelegramChatData,
    ]:
        pass

class StatisticianSocNetOld:
    def __init__(
        self,
        proxy=None,
        file_storage: str | None = None,
        telegram_account=None,
    ):
        self._proxy = proxy
        self._telegram_account = telegram_account

        self._file_settings = (
            StorageManager(file_storage) if file_storage is not None else None
        )

        if self._proxy is not None:
            self._proxy_balancer = ProxyBalancer(self._proxy)
        else:
            self._proxy_balancer = None

        if self._telegram_account is not None:
            self._telegram_account_balancer = TelegramBalancer(self._telegram_account)
        else:
            self._telegram_account_balancer = None

    def get_data(
        self, link
    ) -> Union[
        YouTubeContentData,
        YouTubeChannelsData,
        InstagramContentData,
        TelegramPostData,
        TelegramChatData,
    ]:
        pass

    async def get_data_async(
        self, link
    ) -> Union[
        YouTubeContentData,
        YouTubeChannelsData,
        InstagramContentData,
        TelegramPostData,
        TelegramChatData,
    ]:
        pass

    @staticmethod
    def is_coroutine(func: Callable):
        return inspect.iscoroutinefunction(func)

    @staticmethod
    def get_basic_data(link: str):
        data = ContentAnalyzer().get_data(link)
        return data

    def get_statistician_object(
        self,
        social_network: ResultAnalytics,
    ) -> Type[StatisticianModuleStrategy] | None:
        match (social_network.social_network, social_network.content_type):
            case ("youtube", "video"):
                return YouTubeContent
            case ("youtube", "channel"):
                return YouTubeChannel
            case ("telegram", "chat"):
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
