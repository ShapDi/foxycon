from abc import ABC

from foxycon.data_structures.analysis_type import ResultAnalytics
from foxycon.data_structures.statistician_type import (
    YouTubeChannelsData,
    YouTubeContentData,
    InstagramContentData,
    InstagramPageData,
)
from foxycon.statistics_services.modules.statistics_instagram import InstagramReels
from foxycon.statistics_services.modules.statistics_youtube import (
    YouTubeChannel,
    YouTubeContent,
)


class StatisticianModuleStrategy(ABC):
    def __init__(self, proxy=None, subtitles=None):
        self._proxy = proxy
        self._subtitles = subtitles

    @staticmethod
    def get_data(object_sn):
        pass


class InstagramStatistician(StatisticianModuleStrategy):
    def __init__(self, proxy=None, subtitles=None):
        super().__init__(proxy)
        self._proxy = proxy
        self._subtitles = subtitles

    async def get_data(self, object_sn: ResultAnalytics):
        if object_sn.content_type == "reel":
            data = await InstagramReels(object_sn.url, proxy=self._proxy).get_data()

            return InstagramContentData(
                system_id=data.media_id,
                publish_date=data.publish_date,
                code_id=data.code,
                title=data.description,
                views=data.view_count,
                likes=data.like_count,
                play_count=data.play_count,
                duration=data.duration,
                author=InstagramPageData(
                    user_id=data.author.user_id,
                    username=data.author.username,
                    full_name=data.author.full_name,
                    page_url=f"https://www.instagram.com/" f"{data.author.username}",
                ),
                analytics_obj=object_sn,
            )

    def __str__(self):
        return "instagram"


class YouTubeStatistician(StatisticianModuleStrategy):
    def __init__(self, proxy=None, subtitles=None):
        super().__init__(proxy)
        self._proxy = proxy
        self._subtitles = subtitles
        if self._proxy is not None:
            self._proxy = {
                "http": self._proxy,
                "https": self._proxy,
            }

    def get_data(self, object_sn: ResultAnalytics, proxy=None):
        if object_sn.content_type == "channel":
            data = YouTubeChannel(object_sn.url, proxy=self._proxy)
            return YouTubeChannelsData(
                name=data.name,
                link=data.link,
                description=data.name,
                country=data.country,
                channel_id=data.code,
                view_count=data.view_count,
                subscriber=data.subscriber,
                analytics_obj=object_sn,
                pytube_ob=data.object_channel,
            )
        elif object_sn.content_type == "video":
            data = YouTubeContent(
                object_sn.url, proxy=self._proxy, subtitles=self._subtitles
            )
            return YouTubeContentData(
                title=data.title,
                likes=data.likes,
                link=data.link,
                channel_id=data.code,
                views=data.views,
                system_id=data.system_id,
                channel_url=data.channel_url,
                publish_date=data.publish_date,
                subtitles=data.subtitles,
                analytics_obj=object_sn,
                pytube_ob=data.object_youtube,
            )
        elif object_sn.content_type == "shorts":
            data = YouTubeContent(
                object_sn.url, proxy=self._proxy, subtitles=self._subtitles
            )
            return YouTubeContentData(
                title=data.title,
                likes=data.likes,
                link=data.link,
                channel_id=data.code,
                views=data.views,
                system_id=data.system_id,
                channel_url=data.channel_url,
                publish_date=data.publish_date,
                subtitles=data.subtitles,
                analytics_obj=object_sn,
                pytube_ob=data.object_youtube,
            )

    def __str__(self):
        return "youtube"
