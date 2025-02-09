from telethon.errors import (
    UserPrivacyRestrictedError,
    ChatWriteForbiddenError,
    FloodWaitError,
)
from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantRequest

from foxycon.data_structures.error_type import Telegram


class TelegramPost:
    def __init__(self, url: str, clients_handler):
        self.url = url
        self.client = clients_handler

    async def get_data(self):
        data = {}
        try:
            async with self.client as client:
                parts = self.url.replace("https://t.me/", "").split("/")

                channel_username, message_id = parts[0], int(parts[1])
                # participants = await client.get_participants(int(channel_username))
                # print(participants)
                # for participant in participants:
                #     print(f"User ID: {participant.id}, Username: {participant.username}")

                try:
                    channel = await client.get_entity(channel_username)

                    if not channel.username:
                        try:
                            me = await client.get_me()
                            await client(GetParticipantRequest(channel, me))
                        except Exception as ex:
                            try:
                                await client(JoinChannelRequest(channel))
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


class TelegramGroup:
    def __init__(self, url: str, clients_handler):
        self.url = url
        self.client = clients_handler

    async def get_data(self):
        async with self.client as client:
            parts = self.url.replace("https://t.me/", "").split("/")
            chat = await client.get_entity((int(parts[0])))
            participants = await client.get_participants(int(parts[0]))
            for i in participants:
                print(i)
            data = {
                "chat_id": chat.id,
                "title": chat.title,
                "participants_count": chat.participants_count,
                "date_create": chat.date,
                "users": participants,
            }
            return data
