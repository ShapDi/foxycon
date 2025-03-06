from abc import ABC, abstractmethod

from foxycon.data_structures.analysis_type import ResultAnalytics
from foxycon.data_structures.statistician_type import (
    YouTubeChannelsData,
    YouTubeContentData,
    InstagramContentData,
    InstagramPageData,
    TelegramPostData,
    TelegramChatData,
)
from foxycon.statistics_services.modules.statistics_instagram import InstagramReels
from foxycon.statistics_services.modules.statistics_youtube import (
    YouTubeChannel,
    YouTubeContent,
)
from foxycon.statistics_services.modules.statistics_telegram import (
    TelegramPost,
    TelegramGroup,
)


class StatisticianModuleStrategy(ABC):
    def __init__(self, proxy=None, subtitles=None):
        self._proxy = proxy
        self._subtitles = subtitles

    @abstractmethod
    def get_data(self, object_sn, clients_handlers=None):
        pass

    @abstractmethod
    async def get_data_async(self, object_sn, clients_handlers=None):
        pass


class InstagramStatistician(StatisticianModuleStrategy):
    def __init__(self, proxy=None, subtitles=None):
        super().__init__(proxy)
        self._proxy = proxy
        self._subtitles = subtitles

    async def get_data_async(self, object_sn: ResultAnalytics, clients_handlers=None):
        if object_sn.content_type == "reel":
            data = await InstagramReels(
                object_sn.url, proxy=self._proxy
            ).get_statistics_async()

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
                    page_url=f"https://www.instagram.com/{data.author.username}",
                ),
                analytics_obj=object_sn,
            )

    def get_data(self, object_sn: ResultAnalytics, clients_handlers=None):
        if object_sn.content_type == "reel":
            data = InstagramReels(object_sn.url, proxy=self._proxy).get_statistics()

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
                    page_url=f"https://www.instagram.com/{data.author.username}",
                ),
                analytics_obj=object_sn,
            )


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

    def get_data(
        self, object_sn: ResultAnalytics, clients_handlers=None
    ) -> None | YouTubeContentData | YouTubeChannelsData | Exception:
        if object_sn.content_type == "channel":
            data_channel = YouTubeChannel(object_sn.url, proxy=self._proxy)
            return YouTubeChannelsData(
                name=data_channel.name,
                link=data_channel.link,
                description=data_channel.name,
                country=data_channel.country,
                channel_id=data_channel.code,
                view_count=data_channel.view_count,
                subscriber=data_channel.subscriber,
                data_create=data_channel.data_create,
                number_videos=data_channel.number_videos,
                analytics_obj=object_sn,
                pytube_ob=data_channel.object_channel,
            )
        elif object_sn.content_type == "video":
            try:
                data_content = YouTubeContent(
                    object_sn.url, proxy=self._proxy, subtitles=self._subtitles
                )
            except Exception as ex:
                return ex
            return YouTubeContentData(
                title=data_content.title,
                likes=data_content.likes,
                link=data_content.link,
                channel_id=data_content.code,
                views=data_content.views,
                system_id=data_content.system_id,
                channel_url=data_content.channel_url,
                publish_date=data_content.publish_date,
                subtitles=data_content.subtitles,
                analytics_obj=object_sn,
                pytube_ob=data_content.object_youtube,
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
        return None

    async def get_data_async(self, object_sn: ResultAnalytics, clients_handlers=None):
        if object_sn.content_type == "channel":
            data_channel = YouTubeChannel(object_sn.url, proxy=self._proxy)
            return YouTubeChannelsData(
                name=data_channel.name,
                link=data_channel.link,
                description=data_channel.name,
                country=data_channel.country,
                channel_id=data_channel.code,
                view_count=data_channel.view_count,
                subscriber=data_channel.subscriber,
                data_create=data_channel.data_create,
                number_videos=data_channel.number_videos,
                analytics_obj=object_sn,
                pytube_ob=data_channel.object_channel,
            )
        elif object_sn.content_type == "video":
            try:
                data_content = YouTubeContent(
                    object_sn.url, proxy=self._proxy, subtitles=self._subtitles
                )
            except Exception as ex:
                return ex
            return YouTubeContentData(
                title=data_content.title,
                likes=data_content.likes,
                link=data_content.link,
                channel_id=data_content.code,
                views=data_content.views,
                system_id=data_content.system_id,
                channel_url=data_content.channel_url,
                publish_date=data_content.publish_date,
                subtitles=data_content.subtitles,
                analytics_obj=object_sn,
                pytube_ob=data_content.object_youtube,
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


class TelegramStatistician(StatisticianModuleStrategy):
    def __init__(self, proxy=None, subtitles=None):
        super().__init__(proxy)
        self._proxy = proxy
        self._subtitles = subtitles

    def get_data(
        self, object_sn: ResultAnalytics, clients_handlers=None
    ) -> TelegramPostData | TelegramChatData:
        if object_sn.content_type == "post":
            data = TelegramPost(object_sn.url, clients_handlers).get_statistics()
            return TelegramPostData(
                analytics_obj=object_sn, text=data.get("text"), views=data.get("views")
            )
        else:
            data = TelegramGroup(object_sn.url, clients_handlers).get_statistics()
            return TelegramChatData(
                analytics_obj=object_sn,
                chat_id=data.get("chat_id"),
                title=data.get("title"),
                participants_count=data.get("participants_count"),
                date_create=data.get("date_create"),
            )

    async def get_data_async(
        self, object_sn: ResultAnalytics, clients_handlers=None
    ) -> TelegramPostData | TelegramChatData:
        if object_sn.content_type == "post":
            data = await TelegramPost(
                object_sn.url, clients_handlers
            ).get_statistics_async()
            return TelegramPostData(
                analytics_obj=object_sn, text=data.get("text"), views=data.get("views"), date=data.get('date'),
            )
        else:
            data = await TelegramGroup(
                object_sn.url, clients_handlers
            ).get_statistics_async()
            return TelegramChatData(
                analytics_obj=object_sn,
                chat_id=data.get("chat_id"),
                title=data.get("title"),
                participants_count=data.get("participants_count"),
                date_create=data.get("date_create"))