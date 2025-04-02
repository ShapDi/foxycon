from abc import ABC
from typing import Generator

from foxycon import StatisticianSocNet
from foxycon.data_structures.search_types import TgStatMessage, TelegramUserData
from foxycon.search_services.modules.link_collectors import YouTubeRecCollectorLink
from foxycon.search_services.modules.search_soc_net import YoutubeSearch


class SearchStrategy(ABC):
    pass


class Search:
    def __init__(self, statistician_object: StatisticianSocNet):
        self.statistician_object = statistician_object

    def youtube_search_recommendation(self):
        pass

    async def youtube_search_recommendation_async(self, link):
        data_youtube = await self.statistician_object.get_data_async(link)
        return YouTubeRecCollectorLink(
            statistician_socnet_object=self.statistician_object,
            object_statistic=data_youtube,
        ).get_search_generator_async()





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


class YouTubeSearch:
    def __init__(self, statistician_object: StatisticianSocNet):
        self.statistician_object = statistician_object

    def search_recommendation(self):
        pass

    async def search_recommendation_async(self, link):
        data_youtube = await self.statistician_object.get_data_async(link)
        return YouTubeRecCollectorLink(
            statistician_socnet_object=self.statistician_object,
            object_statistic=data_youtube,
        ).get_search_generator_async()


class TelegramSearch(SearchStrategy):
    def __init__(self, statistician_object: StatisticianSocNet):
        self.statistician_object = statistician_object

    def channel_search(self, link, text):
        pass

    async def channel_search_async(self, link, text):
        data = await self.statistician_object.get_data_async(link)
        print(data)
        client = self.statistician_object._telegram_account_balancer.call_next()
        print(client)
        async with client as client:
            base = []
            async for message in client.iter_messages(
                data.analytics_obj.code, search=text
            ):
                ms = TgStatMessage(
                    telegram_chat_data=data,
                    link_message=f"{data.analytics_obj.url}/{message.id}",
                    date_publication=message.date,
                    message=message.message,
                    views=message.views,
                )
                base.append(ms)
                print(ms)
            return base

    async def get_user_chat(self, link):
        parts = link.replace("https://t.me/", "").split("/")
        client = self.statistician_object._telegram_account_balancer.call_next()
        async with client as client:
            try:
                participants = await client.get_participants(int(parts[0]))
            except:
                participants = await client.get_participants(parts[0])
            users = []
            for user in participants:
                users.append(
                    TelegramUserData(
                        user_id=user.id,
                        bot=user.bot,
                        username=user.username,
                        first_name=user.first_name,
                        last_name=user.last_name,
                    )
                )
            return users
