import re
from abc import ABC, abstractmethod
import urllib.parse

from foxycon.data_structures.content_type import Instagram, YouTube, TikTok


class AnalyzerModuleStrategy(ABC):
    @staticmethod
    @abstractmethod
    def get_code(link):
        pass

    @staticmethod
    @abstractmethod
    def clean_link(link):
        pass

    @staticmethod
    @abstractmethod
    def get_type_content(link):
        pass

    @abstractmethod
    def get_data(self, link):
        pass


class InstagramAnalyzer(AnalyzerModuleStrategy):
    @staticmethod
    def get_code(link):
        match = re.search(r"/(p|reel|reels)/([^/?]+)", link)
        if match:
            return match.group(2)

        page_match = re.search(r"instagram\.com/([^/?]+)", link)
        return page_match.group(1) if page_match else None

    @staticmethod
    def clean_link(link):
        parsed_url = urllib.parse.urlparse(link)
        clean_link = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        return clean_link

    @staticmethod
    def get_type_content(link):
        if "/reel/" in link:
            return Instagram.reel.value
        if "/reels/" in link:
            return Instagram.reel.value
        elif "/p/" in link:
            return Instagram.post.value
        elif "instagram.com/" in link:
            return Instagram.page.value
        else:
            return "unknown"

    def get_data(self, link):
        return {
            "clean_link": self.clean_link(link),
            "type_content": self.get_type_content(link),
            "social_network": "instagram",
            "code": self.get_code(link),
        }


class TikTokAnalyzer(AnalyzerModuleStrategy):
    @staticmethod
    def get_code(link):
        match = re.search(r"/video/([^/?]+)", link)
        if match:
            return match.group(1)

        page_match = re.search(r"tiktok\.com/@([^/?]+)", link)
        return page_match.group(1) if page_match else None

    @staticmethod
    def clean_link(link):
        parsed_url = urllib.parse.urlparse(link)
        clean_link = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        return clean_link

    @staticmethod
    def get_type_content(link):
        if "/video/" in link:
            return TikTok.video.value
        elif "/@" in link:
            return TikTok.page.value
        else:
            return "unknown"

    def get_data(self, link):
        return {
            "clean_link": self.clean_link(link),
            "type_content": self.get_type_content(link),
            "social_network": "tiktok",
            "code": self.get_code(link),
        }


class YouTubeAnalyzer(AnalyzerModuleStrategy):
    @staticmethod
    def get_code(link):
        parsed_url = urllib.parse.urlparse(link)
        if "watch" in parsed_url.path:
            query_params = urllib.parse.parse_qs(parsed_url.query)
            return query_params.get("v")[0].split("?")[0]
        elif "shorts" in parsed_url.path:
            return parsed_url.path.split("/shorts/")[1].split("?")[0]
        elif "@" in parsed_url.path:
            return parsed_url.path.split("@")[1]
        elif "channel" in parsed_url.path:
            return parsed_url.path.split("channel/")[1]
        elif "/" in parsed_url.path:
            return parsed_url.path.split("/")[1]
        return None

    @staticmethod
    def clean_link(link):
        parsed_url = urllib.parse.urlparse(link)
        if "watch" in parsed_url.path:
            query_params = urllib.parse.parse_qs(parsed_url.query)
            return (
                f"https://youtube.com/watch?v={query_params.get('v')[0].split('?')[0]}"
            )
        elif "shorts" in parsed_url.path:
            shorts_id = parsed_url.path.split("/shorts/")[1].split("?")[0]
            return f"https://youtube.com/watch?v={shorts_id}"
        elif "@" in parsed_url.path:
            return f"https://www.youtube.com/@{parsed_url.path.split('@')[1]}"
        elif "channel" in parsed_url.path:
            return (
                f"https://www.youtube.com/channel{parsed_url.path.split('channel')[1]}"
            )
        elif "/" in parsed_url.path:
            shorts_id = parsed_url.path.split("/")[1]
            return f"https://youtube.com/watch?v={shorts_id}"
        return parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path

    @staticmethod
    def get_type_content(link):
        parsed_url = urllib.parse.urlparse(link)
        if "watch" in parsed_url.path:
            return YouTube.video.value
        if "youtu.be" in parsed_url.netloc:
            return YouTube.video.value
        elif "shorts" in parsed_url.path:
            return YouTube.shorts.value
        elif "@" in parsed_url.path or "channel" in parsed_url.path:
            return YouTube.channel.value
        return "unknown"

    def get_data(self, link):
        return {
            "clean_link": self.clean_link(link),
            "type_content": self.get_type_content(link),
            "social_network": "youtube",
            "code": self.get_code(link),
        }


class TelegramAnalyzer(AnalyzerModuleStrategy):
    @staticmethod
    def get_code(link):
        parsed_url = urllib.parse.urlparse(link)
        if len(parsed_url.path.split("/")) == 3:
            return parsed_url.path.split("/")[2]
        else:
            return parsed_url.path.split("/")[1]

    @staticmethod
    def clean_link(link):
        parsed_url = urllib.parse.urlparse(link)
        return parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path

    @staticmethod
    def get_type_content(link):
        parsed_url = urllib.parse.urlparse(link)
        if len(parsed_url.path.split("/")) == 3:
            return "post"
        else:
            return "chat"

    def get_data(self, link):
        return {
            "clean_link": self.clean_link(link),
            "type_content": self.get_type_content(link),
            "social_network": "telegram",
            "code": self.get_code(link),
        }
