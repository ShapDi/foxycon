import os
import json
import random
import time
from abc import ABC, abstractmethod

from requests import session
from telethon import TelegramClient
from telethon.sessions import StringSession


class ClientsHandler(ABC):
    @abstractmethod
    def call_next(self):
        pass


class ProxyBalancer(ClientsHandler):
    def __init__(self, balancing_objects: list):
        self.balancing_objects = []

        for balanc_ob in balancing_objects:
            self.balancing_objects.append(
                {"balanc_ob": balanc_ob, "num_requests": self.get_number_requests()}
            )

    def get_element(self, bal_obj):
        bal_obj["num_requests"] = bal_obj["num_requests"] - 1
        self.balancing_objects.insert(0, bal_obj)
        time.sleep(random.randrange(2, 6, 1))
        return bal_obj.get("balanc_ob")

    def call_next(self):
        bal_obj = self.balancing_objects.pop(0)
        if bal_obj.get("num_requests") == 0:
            bal_obj["num_requests"] = self.get_number_requests()
            self.balancing_objects.append(bal_obj)
            bal_obj = self.balancing_objects.pop(0)

        return self.get_element(bal_obj)

    @staticmethod
    def get_number_requests():
        return random.randrange(2, 5, 1)


class TelegramBalancer(ClientsHandler):
    init_status = False

    def __init__(self, balancing_objects: list):
        self.balancing_objects = balancing_objects

    async def init_call(self):
        for balanc_ob in self.balancing_objects:
            client = TelegramClient(
                api_id=balanc_ob.get("api_id"),
                api_hash=balanc_ob.get("api_hash"),
                session=balanc_ob.get("session"),
            )

            print(balanc_ob)
            if balanc_ob.get("session") is None:
                async with client as temp_client:
                    data_tg_save = self.get_token(api_id=balanc_ob.get("api_id"))
                    if data_tg_save is None:
                        string_session = temp_client.session.save()
                        self.save_token(
                            token=string_session,
                            phone=balanc_ob.get("phone"),
                            api_id=balanc_ob.get("api_id"),
                            api_hash=balanc_ob.get("api_hash"),
                        )
            self.balancing_objects.append(
                {"balanc_ob": client, "num_requests": self.get_number_requests()}
            )



    @staticmethod
    def save_token(token, phone, api_id, api_hash):
        data = {api_id: {"token": token, "phone": phone, "api_hash": api_hash}}
        path_dir = f"{os.getcwd()}/save_token"
        os.mkdir(path_dir)
        with open(f"{path_dir}/token_tg.json", "w+") as token_file:
            token_file.write(json.dumps(data))

    @staticmethod
    def get_token(api_id):
        path_dir = f"{os.getcwd()}/save_token"
        with open(f"{path_dir}/token_tg.json", "w+") as token_file:
            data = json.load(token_file)
            info = data.get(api_id)
        return info

    def get_clients(self):
        if self.init_status is not False:
            self.init_call()
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

    def call_next(self) -> TelegramClient:
        if self.init_status is not False:
            pass
        client = self.clients.pop(0)
        self.clients.append(client)
        client.start(phone="+79152092024")
        # async with client as temp_client:
        #     temp_client
        #     print(
        #         f"ВАЖНО! Сессия для {temp_client.api_id} такая:\n {temp_client.session.save()} \n ОБЯЗАТЕЛЬНО СОХРАНИ ЕЁ!"
        #     )
        return client

    @staticmethod
    def get_number_requests():
        return random.randrange(2, 5, 1)
