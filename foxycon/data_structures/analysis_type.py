from enum import Enum
from dataclasses import dataclass

@dataclass
class ResultAnalytics:
    url: str
    social_network: str
    content_type: str
    code: str


class SocialNetwork(Enum):
    TIKTOK = r"(tiktok\.com)"
    YOUTUBE = r"(youtube\.com)"
    INSTAGRAM = r"(instagram\.com)"
