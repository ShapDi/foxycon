import inspect

from typing import Callable, Type, Union

from telethon import TelegramClient
from telethon.sessions import StringSession
from foxycon.analysis_services.сontent_analyzer import ContentAnalyzer
from foxycon.data_structures.analysis_type import ResultAnalytics
from foxycon.data_structures.statistician_type import (
    YouTubeContentData,
    YouTubeChannelsData,
    TelegramPostData,
    TelegramChatData,
    InstagramContentData,
)
from .modules.interface_statistics_module import StatisticianModuleStrategy

from .modules.statistics_telegram import TelegramGroup, TelegramPost
from .modules.statistics_youtube import YouTubeChannel, YouTubeContent

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
                    proxy = self._entity_balancer.get(Proxy).proxy_str
                    self._entity_balancer.release(proxy)
                except (LookupError, AttributeError):
                    proxy = None
                return YouTubeContent(link=link, proxy=proxy, object_sn=social_network)
            case ("youtube", "channel"):
                try:
                    proxy = self._entity_balancer.get(Proxy).proxy_str
                    self._entity_balancer.release(proxy)
                except (LookupError, AttributeError) as e:
                    proxy = None
                return YouTubeChannel(link=link, proxy=proxy, object_sn=social_network)
            case ("telegram", "chat"):
                telegram_account = self._entity_balancer.get(TelegramAccount)
                self._entity_balancer.release(telegram_account)
                if telegram_account.token_session:
                    telegram_client = TelegramClient(
                        api_id=telegram_account.api_id,
                        api_hash=telegram_account.api_hash,
                        session=StringSession(telegram_account.token_session),
                    )
                else:
                    pass
                return TelegramGroup(url=link, clients_handler=telegram_client)
            case ("telegram", "post"):
                telegram_account = self._entity_balancer.get(TelegramAccount)
                self._entity_balancer.release(telegram_account)
                if telegram_account.token_session:
                    telegram_client = TelegramClient(
                        api_id=telegram_account.api_id,
                        api_hash=telegram_account.api_hash,
                        session=StringSession(telegram_account.token_session),
                    )
                else:
                    pass
                return TelegramPost(url=link, clients_handler=telegram_client)
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
