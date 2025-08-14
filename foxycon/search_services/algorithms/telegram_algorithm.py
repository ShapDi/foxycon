from typing_extensions import override
from socnet_entitys import TelegramAccount
from telethon import TelegramClient
from telethon.sessions import StringSession

from foxycon.data_structures.search_types import TgStatMessage, TelegramUserData
from foxycon.search_services.algorithms.algorithm_interface import SearchAlgorithm
from foxycon.statistics_services.content_social_network import StatisticianSocNet


# class TelegramSearch(SearchAlgorithm):
#     def init(self, statistician_object: StatisticianSocNet):
#         self.statistician_object = statistician_object
#
#
#     async def channel_search_async(self, link, text):
#         data = await self.statistician_object.get_data_async(link)
#         print(data)
#         client = self.statistician_object._telegram_account_balancer.call_next()
#         print(client)
#         async with client as client:
#             base = []
#             async for message in client.iter_messages(data.analytics_obj.code, search=text):
#                 ms = TgStatMessage(telegram_chat_data = data , link_message= f"{data.analytics_obj.url}/{message.id}" , date_publication=message.date ,m>
#                 base.append(ms)
#                 print(ms)
#             return base
#
#     async def get_user_chat(self, link):
#         parts = link.replace("https://t.me/", "").split("/")
#         client = self.statistician_object._telegram_account_balancer.call_next()
#         async with client as client:
#             try:
#                 participants = await client.get_participants(int(parts[0]))
#             except:
#                 participants = await client.get_participants(parts[0])
#             users = []
#             for user in participants:
#                 users.append(TelegramUserData(user_id=user.id, bot=user.bot, username=user.username, first_name=user.first_name, last_name=user.last_name))
#             return users


class TelegramAlgorithmUsers(SearchAlgorithm):
    def __init__(self, link_start: str):
        self._link_start = link_start
        self._statistician_socnet_object: StatisticianSocNet | None = None

    @override
    def init_statistic_engine(self, statistician_socnet_object: StatisticianSocNet):
        self._statistician_socnet_object = statistician_socnet_object
        return self

    def get_participants(self):
        parts = self._link_start.replace("https://t.me/", "").split("/")
        telegram_account = self._statistician_socnet_object._entity_balancer.get(
            TelegramAccount
        )
        telegram_account = TelegramClient(
            api_id=int(telegram_account.api_id),
            api_hash=str(telegram_account.api_hash),
            session=StringSession(str(telegram_account.token_session)),
        )
        with telegram_account as client:
            try:
                participants = client.get_participants(int(parts[0]))
            except:
                participants = client.get_participants(parts[0])
        return participants

    def create_generator(self):
        participants = self.get_participants()
        for user in participants:
            yield TelegramUserData(
                user_id=user.id,
                bot=user.bot,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
            )

    def get_search_generator(self):
        return self.create_generator


# class TelegramAlgorithmMessages(SearchAlgorithm):
#     def __init__(self, link_start: str):
#         self._link_start = link_start
#         self._statistician_socnet_object: StatisticianSocNet | None = None
#
#     @override
#     def init_statistic_engine(self, statistician_socnet_object: StatisticianSocNet):
#         self._statistician_socnet_object = statistician_socnet_object
#         return self
#
#     @override
#     def create_generator(self):
#         parts = self._link_start.replace("https://t.me/", "").split("/")
#         telegram_account = self._statistician_socnet_object._entity_balancer.get(
#             TelegramAccount
#         )
#         telegram_account = TelegramClient(
#             api_id=int(telegram_account.api_id),
#             api_hash=str(telegram_account.api_hash),
#             session=StringSession(str(telegram_account.token_session)),
#         )
#         with telegram_account as client:
#             for message in client.iter_messages(data.analytics_obj.code, search=text):
#                 ms = TgStatMessage(telegram_chat_data = data , link_message= f"{data.analytics_obj.url}/{message.id}" , date_publication=message.date ,m>
#                 base.append(ms)
#                 print(ms)
