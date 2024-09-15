import re
from abc import ABC, abstractmethod
from pytube import YouTube


class StatisticianModuleStrategy(ABC):
    pass


class InstagramStatistician:
    def __init__(self):
        pass

    def __str__(self):
        return 'instagram'


class InstagramPostStatistician:
    pass


class InstagramReelsStatistician:
    pass


class TikTokStatistician:
    def __str__(self):
        return 'tiktok'


class TikTokVideoStatistician:
    pass


class TikTokPageStatistician:
    pass


class YouTubeStatistician:
    def __str__(self):
        return 'youtube'

    def get_data(self, ):
        pass


class YouTubeChannelStatistician:
    pass


class YouTubeVideoStatistician:
    pass
