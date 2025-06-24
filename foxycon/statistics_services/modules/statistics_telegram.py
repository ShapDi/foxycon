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


class TelegramPost(StatisticianModuleStrategy):
    def __init__(self, url: str, clients_handler):
        self.url = url
        self.client = clients_handler

    def get_data(self):
        data = {}
        try:
            with self.client as client:
                parts = self.url.replace("https://t.me/", "").split("/")
                channel_username, message_id = parts[0], int(parts[1])

                try:
                    channel = client.get_entity(channel_username)

                    if not channel.username:
                        try:
                            me = client.get_me()
                            client(GetParticipantRequest(channel, me))
                        except Exception:
                            try:
                                client(JoinChannelRequest(channel))
                                data["error"] = Telegram.JoinChannelRequestSend
                                return data
                            except UserPrivacyRestrictedError:
                                data["error"] = Telegram.UserPrivacyRestrictedError
                                return data
                            except ChatWriteForbiddenError:
                                data["error"] = Telegram.ChatWriteForbiddenError
                                return data
                            except Exception as e:
                                data["error"] = Telegram.General
                                data["error_message"] = e
                                return data

                    try:
                        message = client.get_messages(channel, ids=message_id)
                        if message:
                            data["views"] = message.views
                            data["text"] = message.text
                            data["channel_id"] = message.peer_id.channel_id
                            data["date"] = message.peer_id.date
                            return data
                        else:
                            data["error"] = Telegram.PostNotFound
                            return data
                    except Exception as e:
                        data["error"] = Telegram.General
                        data["error_message"] = e
                        return data

                except Exception as e:
                    data["error"] = Telegram.General
                    data["error_message"] = e
                    return data

        except FloodWaitError as e:
            data["error"] = Telegram.FloodWaitError
            data["error_message"] = e
            return data
        except Exception as e:
            data["error"] = Telegram.General
            data["error_message"] = e
            return data

    async def get_data_async(self):
        data = {}
        try:
            async with self.client as client:
                parts = self.url.replace("https://t.me/", "").split("/")
                channel_username, message_id = parts[0], int(parts[1])
                try:
                    channel = await client.get_entity(channel_username)

                    if not channel.username:
                        try:
                            me = client.get_me()
                            client(GetParticipantRequest(channel, me))
                        except Exception:
                            try:
                                client(JoinChannelRequest(channel))
                                data["error"] = Telegram.JoinChannelRequestSend
                                return data
                            except UserPrivacyRestrictedError:
                                data["error"] = Telegram.UserPrivacyRestrictedError
                                return data
                            except ChatWriteForbiddenError:
                                data["error"] = Telegram.ChatWriteForbiddenError
                                return data
                            except Exception as e:
                                data["error"] = Telegram.General
                                data["error_message"] = e
                                return data

                    try:
                        message = await client.get_messages(channel, ids=message_id)
                        print(message)
                        if message:
                            data["views"] = message.views
                            data["text"] = message.text
                            data["chat_id"] = message.peer_id.channel_id
                            data["date"] = message.date
                            return data
                        else:
                            data["error"] = Telegram.PostNotFound
                            return data
                    except Exception as e:
                        data["error"] = Telegram.General
                        data["error_message"] = e
                        return data

                except Exception as e:
                    data["error"] = Telegram.General
                    data["error_message"] = e
                    return data

        except FloodWaitError as e:
            data["error"] = Telegram.FloodWaitError
            data["error_message"] = e
            return data
        except Exception as e:
            data["error"] = Telegram.General
            data["error_message"] = e
            return data


class TelegramGroup(StatisticianModuleStrategy):
    def __init__(self, url: str, clients_handler: TelegramClient):
        self.url = url
        self.client = clients_handler

    async def get_data_async(self):
        async with self.client as client:
            parts = self.url.replace("https://t.me/", "").split("/")
            try:
                chat = await client.get_entity((int(parts[0])))
            except Exception as ex:
                chat = await client.get_entity(parts[0])
            result = await client(
                functions.channels.GetFullChannelRequest(channel=parts[0])
            )
            data = {
                "chat_id": chat.id,
                "title": chat.title,
                "participants_count": result.full_chat.participants_count,
                "date_create": chat.date,
            }
            return data

    def get_data(self):
        with self.client as client:
            parts = self.url.replace("https://t.me/", "").split("/")
            try:
                chat = client.get_entity((int(parts[0])))
            except Exception as ex:
                chat = client.get_entity(parts[0])
            result = client(functions.channels.GetFullChannelRequest(channel=parts[0]))
            data = {
                "chat_id": chat.id,
                "title": chat.title,
                "participants_count": result.full_chat.participants_count,
                "date_create": chat.date,
            }
            return data
