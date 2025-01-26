# from abc import ABC, abstractmethod
#
# from telethon import TelegramClient
# from telethon.sessions import StringSession
#
#
# class ClientsHandler(ABC):
#     @abstractmethod
#     def get_next(self):
#         pass
#
#
# class TelegramHandler(ClientsHandler):
#     def __init__(self):
#         self.clients = self._get_clients()
#
#     def _get_clients(self):
#         accounts = settings.get_telegram_accounts()
#         clients = []
#         for account in accounts:
#             api_id = account["api_id"]
#             api_hash = account["api_hash"]
#             session = account["session"]
#             string_session = (
#                 StringSession(session)
#                 if session is not None or session != ""
#                 else StringSession()
#             )
#             client = TelegramClient(
#                 api_id=api_id, api_hash=api_hash, session=string_session
#             )
#             if session is None or session == "":
#                 with client as temp_client:
#                     print(
#                         f"ВАЖНО! Сессия для {api_id} такая:\n {temp_client.session.save()} \n ОБЯЗАТЕЛЬНО СОХРАНИ ЕЁ!"
#                     )
#             clients.append(client)
#
#         return clients
#
#     def get_next(self) -> TelegramClient:
#         client = self.clients.pop(0)
#         self.clients.append(client)
#         return client
#
#     def __str__(self):
#         return "telegram_clients_handler"
