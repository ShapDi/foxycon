from telethon.errors import (
    UserPrivacyRestrictedError,
    ChatWriteForbiddenError,
    FloodWaitError,
)
from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantRequest
from telethon import TelegramClient

from foxycon.data_structures.error_type import Telegram

from telethon.sync import functions

from .interface_statistics_module import StatisticianModuleStrategy
from ...data_structures.analysis_type import ResultAnalytics
from ...data_structures.statistician_type import TelegramChatData, TelegramPostData


class TelegramPost(StatisticianModuleStrategy):
    def __init__(self, url: str, clients_handler, analytics_obj: ResultAnalytics):
        self._url = url
        self._client = clients_handler
        self._analytics_obj = analytics_obj

    def get_data(self) -> TelegramPostData:
        with self._client as client:
            parts = self._url.replace("https://t.me/", "").split("/")
            channel_username, message_id = parts[0], int(parts[1])

            channel = client.get_entity(channel_username)

            if not channel.username:
                me = client.get_me()
                client(GetParticipantRequest(channel, me))

            message = client.get_messages(channel, ids=message_id)
            return TelegramPostData(
                analytics_obj=self._analytics_obj,
                views=message.views,
                text=message.text,
                date=message.date,
                chat_id=message.peer_id.channel_id,
            )

    async def get_data_async(self) -> TelegramPostData:
        async with self._client as client:
            parts = self._url.replace("https://t.me/", "").split("/")
            channel_username, message_id = parts[0], int(parts[1])

            channel = await client.get_entity(channel_username)

            if not channel.username:
                me = client.get_me()
                client(GetParticipantRequest(channel, me))

            message = await client.get_messages(channel, ids=message_id)
            return TelegramPostData(
                analytics_obj=self._analytics_obj,
                views=message.views,
                text=message.text,
                date=message.date,
                chat_id=message.peer_id.channel_id,
            )


class TelegramGroup(StatisticianModuleStrategy):
    def __init__(
        self, url: str, clients_handler: TelegramClient, analytics_obj: ResultAnalytics
    ):
        self._url = url
        self._client = clients_handler
        self._analytics_obj = analytics_obj

    async def get_data_async(self):
        async with self._client as client:
            parts = self._url.replace("https://t.me/", "").split("/")
            try:
                chat = await client.get_entity((int(parts[0])))
            except Exception as ex:
                chat = await client.get_entity(parts[0])
            result = await client(
                functions.channels.GetFullChannelRequest(channel=parts[0])
            )
            return TelegramChatData(
                analytics_obj=self._analytics_obj,
                chat_id=chat.id,
                title=chat.title,
                participants_count=result.full_chat.participants_count,
                date_create=chat.date,
            )

    def get_data(self):
        with self._client as client:
            parts = self._url.replace("https://t.me/", "").split("/")
            try:
                chat = client.get_entity((int(parts[0])))
            except Exception as ex:
                chat = client.get_entity(parts[0])
            result = client(functions.channels.GetFullChannelRequest(channel=parts[0]))
            return TelegramChatData(
                analytics_obj=self._analytics_obj,
                chat_id=chat.id,
                title=chat.title,
                participants_count=result.full_chat.participants_count,
                date_create=chat.date,
            )
