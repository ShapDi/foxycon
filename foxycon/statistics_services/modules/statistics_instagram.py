import re
from abc import ABC, abstractmethod

from instagram_tail import InstagramApi


class SocialNetworkParsingObject(ABC):
    @abstractmethod
    def get_statistics(self):
        pass

    @abstractmethod
    async def get_statistics_async(self):
        pass


class InstagramReels(SocialNetworkParsingObject):
    def __init__(self, link, proxy):
        self._link = link
        self._proxy = proxy

    @staticmethod
    def get_code(url):
        match = re.search(r"/reel[s]?/([^/?#&]+)", url)
        if match:
            return match.group(1)
        else:
            return None

    def get_statistics(self):
        client = InstagramApi().get_client()
        code = self.get_code(self._link)
        data = client(proxy=self._proxy).reel(code)
        return data

    async def get_statistics_async(self):
        client = InstagramApi().get_client()
        code = self.get_code(self._link)
        data = client(proxy=self._proxy).reel(code)
        return data
