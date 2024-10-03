from enum import Enum


class Instagram(Enum):
    reel = 'reel'
    reels = 'reels'
    post = 'post'
    page = 'page'


class Twitter(Enum):
    page = 'page'
    status = 'post'


class VK(Enum):
    reel = 'reel'
    wall = 'post'
    page = 'page'
    photo = 'photo'


class YouTube(Enum):
    shorts = 'shorts'
    video = 'video'
    channel = 'channel'


class TikTok(Enum):
    video = 'video'
    page = 'page'
