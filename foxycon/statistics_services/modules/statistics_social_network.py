from abc import ABC

from foxycon.data_structures.analysis_type import ResultAnalytics
from foxycon.data_structures.statistician_type import YouTubeChannelsData, YouTubeContentData
from foxycon.statistics_services.modules.statistics_instagram import InstagramReels
from foxycon.statistics_services.modules.statistics_youtube import YouTubeChannel, YouTubeContent


class StatisticianModuleStrategy(ABC):
    def __init__(self, proxy=None):
        self._proxy = proxy

    @staticmethod
    def get_data(object_sn):
        pass


class InstagramStatistician(StatisticianModuleStrategy):

    def __init__(self, proxy=None):
        super().__init__(proxy)
        self._proxy = proxy

    @staticmethod
    async def get_data(object_sn: ResultAnalytics):
        if object_sn.content_type == 'reel':
            data = await InstagramReels(object_sn.link).get_data()
            return data

    def __str__(self):
        return 'instagram'


class YouTubeStatistician(StatisticianModuleStrategy):

    def __init__(self, proxy=None):
        super().__init__(proxy)
        self._proxy = proxy

    @staticmethod
    def get_data(object_sn: ResultAnalytics, proxy = None):
        if object_sn.content_type == 'channel':
            data = YouTubeChannel(object_sn.link, proxy=proxy)
            return YouTubeChannelsData(name=data.name,
                                       link=data.link,
                                       description=data.name,
                                       country=data.country,
                                       code=data.code,
                                       view_count=data.view_count,
                                       subscriber=data.subscriber, )
        elif object_sn.content_type == 'video':
            data = YouTubeContent(object_sn.link)
            return YouTubeContentData(title=data.title,
                                      likes=data.likes,
                                      link=data.link,
                                      code=data.code,
                                      views=data.views,
                                      system_id=data.system_id,
                                      channel_url=data.channel_url,
                                      publish_date=data.publish_date)

    def __str__(self):
        return 'youtube'