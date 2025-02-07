import os
import json
import random
import time
from abc import ABC, abstractmethod

from telethon import TelegramClient
from telethon.sessions import StringSession

from foxycon.data_structures.utils_type import TelegramAccount, BalancingObject
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



class TelegBalancer(Balancer):
    NOT_HACKING_PROTECTION = False

    def __init__(self, balancing_objects: list[TelegramAccount | dict]):
        self.balancing_objects = self.get_acc_th(balancing_objects)

    @staticmethod
    def get_number_requests():
        return random.randrange(2, 5, 1)

    def get_acc_th(self, accounts):
        list_accounts = []
        for account in accounts:
            if type(account) == list:
                account = TelegramAccount(
                    api_id=account.get("api_id"),
                    api_hash=account.get("api_hash"),
                    session_token=account.get("session_token"),
                    phone=account.get("phone"),
                    bot_token=account.get("bot_token"),
                    proxy=account.get("proxy"),
                )
            if account is None:
                self.NOT_HACKING_PROTECTION = True
            list_accounts.append(
                BalancingObject(
                    torsion_object=account, num_requests=self.get_number_requests()
                )
            )
        return list_accounts

    @staticmethod
    def storage_check() -> bool:
        return os.path.exists(f"{os.getcwd()}/storage/tg_account.json")

    @staticmethod
    def account_inside_storage_check(
        api_id: int, session_token: str | None = None
    ) -> TelegramAccount | bool:
        pass

    @staticmethod
    async def add_account_storage(telegram_account: TelegramAccount):
        async with open(f"{os.getcwd()}/storage/tg_account.json") as tg_account_file:
            tg_account_file

    @staticmethod
    async def get_account_storage(telegram_account: TelegramAccount):
        pass

    async def initialization_account(self):
        if self.storage_check():
            pass
        else:
            pass

    async def call_next(self):
        if self.NOT_HACKING_PROTECTION:
            await self.initialization_account()

        bal_obj = self.balancing_objects.pop(0)
        if bal_obj.get("num_requests") == 0:
            bal_obj["num_requests"] = self.get_number_requests()
            self.balancing_objects.append(bal_obj)
            bal_obj = self.balancing_objects.pop(0)

        return self.get_element(bal_obj)




# class TelegramBalancer(Balancer):
#     init_status = False
#
#     def __init__(self, balancing_objects: list):
#         self.balancing_objects = balancing_objects
#         self._clients = []
#
    # async def init_call(self):
    #     for balanc_ob in self.balancing_objects:
    #         client = TelegramClient(
    #             api_id=balanc_ob.get("api_id"),
    #             api_hash=balanc_ob.get("api_hash"),
    #             session=balanc_ob.get("session"),
    #         )
#
#             print(f"Инициализация аккаунта: {balanc_ob.get('phone')}")
#             session_data = self.get_session_data(api_id=balanc_ob.get("api_id"))
#
#             if session_data is None or session_data.get("session") is None:
#                 print(f"Нет сессии для {balanc_ob.get('phone')}, выполняем аутентификацию...")
#                 async with client as temp_client:
#                     string_session = temp_client.session.save()
#                     self.save_session(
#                         session=string_session,
#                         phone=balanc_ob.get("phone"),
#                         api_id=balanc_ob.get("api_id"),
#                         api_hash=balanc_ob.get("api_hash"),
#                     )
#             else:
#                 print(f"Используем сохраненную сессию для {balanc_ob.get('phone')}")
#                 string_session = session_data.get("session")
#                 client.session = StringSession(string_session)
#
#             self._clients.append(client)
#
#     @staticmethod
#     def save_session(session, phone, api_id, api_hash):
#         """
#         Сохранение сессий Telegram аккаунтов в единственный файл
#         """
#         data = {api_id: {"session": session, "phone": phone, "api_hash": api_hash}}
#         path_dir = f"{os.getcwd()}/save_sessions"
#         os.makedirs(path_dir, exist_ok=True)
#
#         # Загружаем данные, если файл уже существует, чтобы обновить информацию
#         file_path = f"{path_dir}/token_tg.json"
#         if os.path.exists(file_path):
#             try:
#                 with open(file_path, "r+") as session_file:
#                     data_existing = json.load(session_file)
#                     data_existing.update(data)
#                     session_file.seek(0)
#                     session_file.write(json.dumps(data_existing))
#             except json.JSONDecodeError:
#                 print(f"Ошибка чтения файла {file_path}")
#                 with open(file_path, "w+") as session_file:
#                     session_file.write(json.dumps(data))
#         else:
#             with open(file_path, "w+") as session_file:
#                 session_file.write(json.dumps(data))
#
#     @staticmethod
#     def get_session_data(api_id):
#         """
#         Получение сохраненной сессии для указанного api_id
#         """
#         path_dir = f"{os.getcwd()}/save_sessions"
#         file_path = f"{path_dir}/token_tg.json"
#
#         # Проверяем существует ли файл с сессиями
#         if os.path.exists(file_path):
#             try:
#                 with open(file_path, "r") as session_file:
#                     data = json.load(session_file)
#                     return data.get(str(api_id))  # Возвращаем данные сессии для этого api_id
#             except json.JSONDecodeError:
#                 print(f"Ошибка чтения файла {file_path}")
#                 return None
#         else:
#             print(f"Файл {file_path} не найден.")
#             return None
#
#     def get_clients(self):
#         """
#         Получение всех инициализированных клиентов
#         """
#         if not self.init_status:
#             raise Exception("Аккаунты еще не инициализированы!")
#
#         return self._clients
#
#     def call_next(self) -> TelegramClient:
#         """
#         Возвращает следующий аккаунт из списка для использования
#         """
#         if not self.init_status:
#             raise Exception("Аккаунты еще не инициализированы!")
#
#         client = self._clients.pop(0)
#         self._clients.append(client)
#         return client
#
#     async def use_multiple_accounts(self):
#         """
#         Использует несколько аккаунтов для выполнения операций.
#         """
#         if not self.init_status:
#             await self.init_call()
#
#         for account in self._clients:
#             async with account as client:
#                 me = await client.get_me()
#                 print(f"Используем аккаунт {me.username}")
#                 await self.some_action(client)
#
#     async def some_action(self, client):
#         """
#         Пример действия с аккаунтом.
#         """
#         print("Выполняем действие с аккаунтом...")
#         # Пример действия: получение информации о текущем пользователе
#         me = await client.get_me()
#         print(f"Информация о пользователе: {me.username}")
#

# Пример использования:

# async def main():
#     # Ваши аккаунты
#     accounts = [
#         {
#             "api_id": 25490814,
#             "api_hash": "0789de556a85e76bf48bd2f65fe1856d",
#             "session": None,
#             "phone": "+79152092024",
#         },
#     ]
#
#     # Создаем объект TelegramBalancer с аккаунтами
#     balancer = TelegramBalancer(accounts)
#
#     # Инициализируем аккаунты
#     await balancer.init_call()
#
#     # Используем несколько аккаунтов
#     await balancer.use_multiple_accounts()

# Запуск
class TelegramBalancer(Balancer):
    def  __init__(self, balancing_objects: list):
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
                    proxy=balancing_object.get("proxy"))
                print(data_tg)
                async with TelegramClient(StringSession(data_tg.session), data_tg.api_id, data_tg.api_hash) as client:
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