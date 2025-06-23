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

# from foxycon.utils.balancers import TelegramBalancer, ProxyBalancer, InstagramBalancer
from .statistics_exceptions import RequiredTelegramAccount
from ..data_structures.balancer_type import Proxy, TelegramAccount, InstagramAccount

from socnet_entitys import (
    EntityPool,
    AsyncEntityBalancer,
    BaseEntityBalancer,
    Proxy,
    TelegramAccount,
    InstagramAccount,
)
from socnet_entitys.entitys import Entity


class StatisticianSocNet:
    def __init__(
        self,
        entity_pool: EntityPool | None = None,
        entity_balancer: BaseEntityBalancer | None = None,
        async_entity_balancer: AsyncEntityBalancer | None = None,
    ):
        self._entity_pool = entity_pool
        self._entity_balancer = entity_balancer
        self._async_entity_balancer = async_entity_balancer

    def get_statistician_object(
        self,
        link,
        social_network: ResultAnalytics,
    ) -> StatisticianModuleStrategy | None:
        match (social_network.social_network, social_network.content_type):
            case ("youtube", "video"):
                proxy = self._entity_balancer.get(Proxy)
                return YouTubeContent(link=link, proxy=proxy, object_sn=social_network)
            case ("youtube", "channel"):
                proxy = self._entity_balancer.get(Proxy)
                return YouTubeChannel(link=link, proxy=proxy, object_sn=social_network)
            case ("telegram", "chat"):
                telegram_account = self._entity_balancer.get(TelegramAccount)
                return TelegramGroup(url=link, clients_handler=telegram_account)
        return None

    @staticmethod
    def get_basic_data(link: str):
        data = ContentAnalyzer().get_data(link)
        return data

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
        link_analytics = self.get_basic_data(link)
        data = self.get_statistician_object(link, link_analytics).get_data()

        return data


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
