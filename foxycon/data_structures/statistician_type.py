from dataclasses import dataclass


@dataclass
class YouTubeContentData:
    title: str
    likes: str
    link: str
    code: str
    views: str
    system_id: str
    channel_url: str
    publish_date: str


@dataclass
class YouTubeChannelsData:
    name: str
    link: str
    description: str
    country: str
    code: str
    view_count: int
    subscriber: int


@dataclass
class InstagramReelsData:
    pass
