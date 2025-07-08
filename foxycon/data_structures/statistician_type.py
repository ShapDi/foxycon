import datetime
from dataclasses import dataclass
from pytubefix import YouTube, Channel
from foxycon.data_structures.analysis_type import ResultAnalytics


@dataclass
class ContentData:
    analytics_obj: ResultAnalytics


@dataclass
class YouTubeContentData(ContentData):
    system_id: str
    channel_id: str
    title: str
    likes: int
    link: str
    views: int
    channel_url: str
    publish_date: datetime.date


@dataclass
class HeavyYouTubeContentData(YouTubeContentData):
    pytube_ob: YouTube


@dataclass
class YouTubeChannelsData(ContentData):
    channel_id: str
    name: str
    link: str
    description: str
    country: str
    view_count: int
    subscriber: int
    number_videos: int
    data_create: datetime.date


@dataclass
class HeavyYouTubeChannelsData(YouTubeChannelsData):
    pytube_ob: Channel


@dataclass
class InstagramPageData:
    user_id: str
    username: str
    full_name: str
    page_url: str


@dataclass
class InstagramContentData(ContentData):
    title: str
    system_id: str
    publish_date: str
    views: int
    likes: int
    play_count: int
    duration: int
    code_id: str
    author: InstagramPageData


@dataclass
class TelegramPostData(ContentData):
    chat_id: int
    text: str
    views: int
    date: datetime


@dataclass
class TelegramChatData(ContentData):
    chat_id: int
    title: str
    participants_count: int
    date_create: datetime.datetime
    # users: list[TelegramUserData]
