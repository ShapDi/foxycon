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
                try:
                    proxy = self._entity_balancer.get(Proxy)
                except (LookupError, AttributeError):
                    proxy = None
                return YouTubeContent(link=link, proxy=proxy, object_sn=social_network)
            case ("youtube", "channel"):
                try:
                    proxy = self._entity_balancer.get(Proxy)
                except (LookupError, AttributeError):
                    proxy = None
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
        link_analytics = self.get_basic_data(link)
        data = await self.get_statistician_object(link, link_analytics).get_data_async()

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
        link_analytics = self.get_basic_data(link)
        data = self.get_statistician_object(link, link_analytics).get_data()

        return data
