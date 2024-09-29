from datetime import datetime
import re

from instagram_reels.main.InstagramAPIClientImpl import InstagramAPIClientImpl


class InstagramReels:
    def __init__(self, link, proxy):
        self._link = link
        self._proxy = proxy

    @staticmethod
    async def get_client():
        client = await InstagramAPIClientImpl().reels()
        return client

    @staticmethod
    async def get_code(url):
        match = re.search(r'/reel[s]?/([^/?#&]+)', url)
        if match:
            return match.group(1)
        else:
            return None

    @staticmethod
    async def unix_to_date(unix_time: int) -> str:
        date_time = datetime.utcfromtimestamp(unix_time)
        formatted_date = date_time.strftime('%d.%m.%Y')
        return formatted_date

    async def get_data(self):
        code = await self.get_code(self._link)
        client = await self.get_client()
        data = await client.get(code, proxy=self._proxy)
        data.publish_date = await self.unix_to_date(data.publish_date)
        return data
