from dataclasses import dataclass
from enum import Enum
@dataclass
class ResultAnalytics:
    link: str
    social_network: str
    content_type: str
    code: str


class SocialNetwork(Enum):
    TIKTOK = r"(tiktok\.com)"
    YOUTUBE = r"(youtube\.com)"
    INSTAGRAM = r"(instagram\.com)"