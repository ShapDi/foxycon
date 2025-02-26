from abc import ABC

from foxycon import StatisticianSocNet
from foxycon.data_structures.search_types import TgStatMessage, TelegramUserData



class SearchStrategy(ABC):
    pass

class YouTubeSearch(SearchStrategy):
    pass


class TelegramSearch(SearchStrategy):
    def __init__(self, statistician_object: StatisticianSocNet):
        self.statistician_object = statistician_object

    def channel_search(self, link, text):
        pass

    async def channel_search_async(self, link, text):
        data = await self.statistician_object.get_data_async(link)
        print(data)
        client = self.statistician_object._telegram_account_balancer.call_next()
        print(client)
        async with client as client:
            base = []
            async for message in client.iter_messages(data.analytics_obj.code, search=text):
                ms = TgStatMessage(telegram_chat_data = data , link_message= f"{data.analytics_obj.url}/{message.id}" , date_publication=message.date ,message= message.message,views=message.views)
                base.append(ms)
                print(ms)
            return base

    async def get_user_chat(self, link):
        parts = link.replace("https://t.me/", "").split("/")
        client = self.statistician_object._telegram_account_balancer.call_next()
        async with client as client:
            try:
                participants = await client.get_participants(int(parts[0]))
            except:
                participants = await client.get_participants(parts[0])
            users = []
            for user in participants:
                users.append(TelegramUserData(user_id=user.id, bot=user.bot, username=user.username, first_name=user.first_name, last_name=user.last_name))
            return users

