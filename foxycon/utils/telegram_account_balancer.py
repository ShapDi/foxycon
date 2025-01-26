import os
import json
from abc import ABC, abstractmethod

from telethon import TelegramClient
from telethon.sessions import StringSession


class ClientsHandler(ABC):
    @abstractmethod
    def get_next(self):
        pass


class TelegramBalancer(ClientsHandler):
    def __init__(self, accounts):
        self._accounts = accounts
        self.clients = self.get_clients()
        self.balancing_objects = []

    @staticmethod
    def save_token(token, phone, api_id, api_hash):
        data = {api_id: {"token": token, "phone": phone, "api_hash": api_hash}}
        path_dir = f"{os.getcwd()}/save_token"
        os.mkdir(path_dir)
        with open(f"{path_dir}/token_tg.json", "w+") as token_file:
            token_file.write(json.dumps(data))

    @staticmethod
    def get_token(api_id):
        pass

    def get_clients(self):
        clients = []
        for account in self._accounts:
            api_id = account["api_id"]
            api_hash = account["api_hash"]
            session = account["session"]
            phone = account["phone"]
            string_session = (
                StringSession(session)
                if session is not None or session != ""
                else StringSession()
            )
            client = TelegramClient(
                api_id=api_id,
                api_hash=api_hash,
                session=string_session,
            )
            clients.append(client)

        return clients

    async def get_next(self) -> TelegramClient:
        client = self.clients.pop(0)
        self.clients.append(client)
        # async with client as temp_client:
        #     temp_client
        #     print(
        #         f"ВАЖНО! Сессия для {temp_client.api_id} такая:\n {temp_client.session.save()} \n ОБЯЗАТЕЛЬНО СОХРАНИ ЕЁ!"
        #     )
        return client

    def __str__(self):
        return "telegram_clients_handler"
