from telethon.errors import (
    UserPrivacyRestrictedError,
    ChatWriteForbiddenError,
    FloodWaitError,
)
from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantRequest

from foxycon.data_structures.error_type import Telegram

from telethon import functions as functions_async
from telethon.sync import functions

from foxycon.statistics_services.modules.statistics_instagram import SocialNetworkParsingObject



class TelegramPost(SocialNetworkParsingObject):
    def __init__(self, url: str, clients_handler):
        self.url = url
        self.client = clients_handler

    def get_statistics(self):
        data = {}
        try:
            with self.client as client:
                parts = self.url.replace("https://t.me/", "").split("/")
                search = "winline"

                try:
                    result = client(
                        functions.contacts.SearchRequest(q=search, limit=100)
                    )
                    print(result)
                except Exception as ex:
                    print(ex)
                channel_username, message_id = parts[0], int(parts[1])
                text = "winline"
                for message in client.iter_messages(channel_username, search=text):
                    parts
                    print(message)
                try:
                    channel = client.get_entity(channel_username)

                    if not channel.username:
                        try:
                            me = client.get_me()
                            client(GetParticipantRequest(channel, me))
                        except Exception as ex:
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
            print(e)
            data["error"] = Telegram.General
            data["error_message"] = e
            return data

    async def get_statistics_async(self):
        data = {}
        try:
           async with self.client as client:
                parts = self.url.replace("https://t.me/", "").split("/")
                search = "winline"

                try:
                    result = await client(
                        functions.contacts.SearchRequest(q=search, limit=100)
                    )
                    print(result)
                except Exception as ex:
                    print(ex)
                channel_username, message_id = parts[0], int(parts[1])
                text = "winline"
                async for message in client.iter_messages(channel_username, search=text):
                    parts
                    print(message)
                try:
                    channel = await client.get_entity(channel_username)

                    if not channel.username:
                        try:
                            me = client.get_me()
                            client(GetParticipantRequest(channel, me))
                        except Exception as ex:
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
            print(e)
            data["error"] = Telegram.General
            data["error_message"] = e
            return data



class TelegramGroup:
    def __init__(self, url: str, clients_handler):
        self.url = url
        self.client = clients_handler

    async def get_statistics_async(self):
        async with self.client as client:
            parts = self.url.replace("https://t.me/", "").split("/")

            chat = await client.get_entity((int(parts[0])))
            # except:
            #     chat = await client.get_entity(parts[0])
            #     print(chat)
            participants = await client.get_participants(int(parts[0]))
            data = {
                "chat_id": chat.id,
                "title": chat.title,
                "participants_count": chat.participants_count,
                "date_create": chat.date,
                "users": participants,
            }
            return data

    def get_statistics(self):
        with self.client as client:
            parts = self.url.replace("https://t.me/", "").split("/")

            chat = client.get_entity((int(parts[0])))
            # except:
            #     chat = await client.get_entity(parts[0])
            #     print(chat)
            participants = client.get_participants(int(parts[0]))
            data = {
                "chat_id": chat.id,
                "title": chat.title,
                "participants_count": chat.participants_count,
                "date_create": chat.date,
                "users": participants,
            }
            return data
