from dataclasses import dataclass
from pytubefix import YouTube, Channel
from foxycon.data_structures.analysis_type import ResultAnalytics


@dataclass
class YouTubeContentData:
    system_id: str
    channel_id: str
    title: str
    likes: str
    link: str
    views: str
    channel_url: str
    publish_date: str
    subtitles: str
    analytics_obj: ResultAnalytics
    pytube_ob: YouTube


@dataclass
class YouTubeChannelsData:
    channel_id: str
    name: str
    link: str
    description: str
    country: str
    view_count: int
    subscriber: int
    analytics_obj: ResultAnalytics
    pytube_ob: Channel


@dataclass
class InstagramPageData:
    user_id: str
    username: str
    full_name: str
    page_url: str


@dataclass
class InstagramContentData:
    title: str
    system_id: str
    publish_date: str
    views: int
    likes: int
    play_count: int
    duration: int
    code_id: str
    author: InstagramPageData
    analytics_obj: ResultAnalytics
