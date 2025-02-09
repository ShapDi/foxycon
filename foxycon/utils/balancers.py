import random
import time
from abc import ABC, abstractmethod

from telethon import TelegramClient
from telethon.sessions import StringSession

from foxycon.data_structures.utils_type import TelegramAccount
from foxycon.utils.storage_manager import StorageManager


class Balancer(ABC):
    @abstractmethod
    def call_next(self):
        pass


class ProxyBalancer(Balancer):
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


class TelegramBalancer(Balancer):
    def __init__(self, balancing_objects: list):
        self.balancing_objects = balancing_objects

    @staticmethod
    def updata(data_tg: TelegramAccount):
        pass

    async def init_call(self):
        old_balancing_objects = self.balancing_objects
        self.balancing_objects = []
        try:
            for balancing_object in old_balancing_objects:
                data_tg = TelegramAccount(
                    api_id=balancing_object.get("api_id"),
                    api_hash=balancing_object.get("api_hash"),
                    session=balancing_object.get("session"),
                    proxy=balancing_object.get("proxy"),
                )
                print(data_tg)
                async with TelegramClient(
                    StringSession(data_tg.session), data_tg.api_id, data_tg.api_hash
                ) as client:
                    string = client.session.save()
                    print(string)
                    data_tg.session = string
                    print(data_tg.session)
                    self.updata(data_tg)
                    self.balancing_objects.append(client)
        except Exception as ex:
            print(ex)

    def call_next(self):
        client = self.balancing_objects.pop(0)
        self.balancing_objects.append(client)
        return client
