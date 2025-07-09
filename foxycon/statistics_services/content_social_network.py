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
from .statistics_exceptions import ParsingNotPossible

from ..data_structures.balancer_type import Proxy, TelegramAccount, InstagramAccount

from socnet_entitys import (
    EntityPool,
    AsyncEntityBalancer,
    BaseEntityBalancer,
    Proxy,
    TelegramAccount,
)


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
        self, link: str, result_analytic: ResultAnalytics, type_data: str
    ) -> StatisticianModuleStrategy | None:
        match (result_analytic.social_network, result_analytic.content_type):
            case ("youtube", "video"):
                try:
                    proxy = self._entity_balancer.get(Proxy)
                    self._entity_balancer.release(proxy)
                    proxy = proxy.proxy_comparison
                except (LookupError, AttributeError):
                    proxy = None
                return YouTubeContent(
                    link=link,
                    proxy=proxy,
                    object_sn=result_analytic,
                    type_data=type_data,
                )
            case ("youtube", "channel"):
                try:
                    proxy = self._entity_balancer.get(Proxy)
                    self._entity_balancer.release(proxy)
                    proxy = proxy.proxy_comparison
                except (LookupError, AttributeError):
                    proxy = None
                return YouTubeChannel(
                    link=link,
                    proxy=proxy,
                    object_sn=result_analytic,
                    type_data=type_data,
                )
            case ("telegram", "chat"):
                telegram_account = self._entity_balancer.get(TelegramAccount)
                self._entity_balancer.release(telegram_account)
                if telegram_account.token_session:
                    telegram_client = TelegramClient(
                        api_id=int(telegram_account.api_id),
                        api_hash=str(telegram_account.api_hash),
                        session=StringSession(str(telegram_account.token_session)),
                    )
                else:
                    raise ParsingNotPossible("Uninitialized telegram account")
                return TelegramGroup(
                    url=link,
                    clients_handler=telegram_client,
                    analytics_obj=result_analytic,
                )
            case ("telegram", "post"):
                telegram_account = self._entity_balancer.get(TelegramAccount)
                self._entity_balancer.release(telegram_account)
                if telegram_account.token_session:
                    telegram_client = TelegramClient(
                        api_id=int(telegram_account.api_id),
                        api_hash=str(telegram_account.api_hash),
                        session=StringSession(str(telegram_account.token_session)),
                    )
                else:
                    raise ParsingNotPossible("Uninitialized telegram account")
                return TelegramPost(
                    url=link,
                    clients_handler=telegram_client,
                    analytics_obj=result_analytic,
                )
        return None

    @staticmethod
    def get_basic_data(link: str):
        data = ContentAnalyzer().get_data(link)
        return data

    async def get_data_async(
        self, link, type_data="static"
    ) -> Union[
        YouTubeContentData,
        YouTubeChannelsData,
        InstagramContentData,
        TelegramPostData,
        TelegramChatData,
    ]:
        link_analytics = self.get_basic_data(link)
        data = await self.get_statistician_object(
            link, link_analytics, type_data
        ).get_data_async()

        return data

    def get_data(
        self, link, type_data="static"
    ) -> Union[
        YouTubeContentData,
        YouTubeChannelsData,
        InstagramContentData,
        TelegramPostData,
        TelegramChatData,
    ]:
        link_analytics = self.get_basic_data(link)
        data = self.get_statistician_object(link, link_analytics, type_data).get_data()

        return data
