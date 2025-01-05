import json
from abc import ABC
import re
from datetime import datetime

from pytubefix import YouTube, Channel
from bs4 import BeautifulSoup
from regex import regex


class RecipientYouTubeAbstract(ABC):
    pass


class YouTubeChannel(RecipientYouTubeAbstract):
    def __init__(self, link, proxy=None):
        self._link = self.transform_youtube_channel_link(link)
        self._proxy = proxy
        self._object_channel = self.get_object_youtube(self._link, self._proxy)
        self.name = self._object_channel.channel_name
        self.link = self._object_channel.channel_url
        self.description = self.get_description()
        self.country = self.get_country()
        self.code = self._object_channel.channel_id
        self.view_count = self.get_view_count()
        self.data_create = self.get_data_create()
        self.number_videos = self.get_number_videos()
        self.subscriber = self.get_subscriber()

    @staticmethod
    def transform_youtube_channel_link(url: str) -> str:
        pattern = r"https://www\.youtube\.com/@([\w-]+)"
        match = re.match(pattern, url)

        if match:
            channel_name = match.group(1)
            return f"https://www.youtube.com/c/{channel_name}/videos"

        else:
            return url

    @staticmethod
    def get_object_youtube(link, proxies) -> Channel:
        channel = Channel(link, proxies)
        return channel

    @staticmethod
    def extract_json(text):
        json_pattern = regex.compile(r"\{(?:[^{}]|(?R))*\}")
        json_matches = json_pattern.findall(str(text))
        extracted_json = []
        for match in json_matches:
            try:
                json_data = json.loads(match)
                extracted_json.append(json_data)
            except json.JSONDecodeError:
                pass
        return extracted_json

    def get_base_con(self):
        soup = BeautifulSoup(self._object_channel.about_html, "html.parser")
        script = soup.find_all("script")
        data = self.extract_json(script)
        return data[4].get("onResponseReceivedEndpoints")

    def get_country(self):
        data = self.get_base_con()
        text_country = (
            data[0]
            .get("showEngagementPanelEndpoint")
            .get("engagementPanel")
            .get("engagementPanelSectionListRenderer")
            .get("content")
            .get("sectionListRenderer")
            .get("contents")[0]
            .get("itemSectionRenderer")
            .get("contents")[0]
            .get("aboutChannelRenderer")
            .get("metadata")
            .get("aboutChannelViewModel")
            .get("country")
        )
        return text_country

    def get_view_count(self):
        data = self.get_base_con()
        text_view_count = (
            data[0]
            .get("showEngagementPanelEndpoint")
            .get("engagementPanel")
            .get("engagementPanelSectionListRenderer")
            .get("content")
            .get("sectionListRenderer")
            .get("contents")[0]
            .get("itemSectionRenderer")
            .get("contents")[0]
            .get("aboutChannelRenderer")
            .get("metadata")
            .get("aboutChannelViewModel")
            .get("viewCountText")
        )
        view_count = Convert.convert_views_to_int(text_view_count)
        return view_count

    def get_number_videos(self):
        data = self.get_base_con()
        number_videos = (
            data[0]
            .get("showEngagementPanelEndpoint", {})
            .get("engagementPanel", {})
            .get("engagementPanelSectionListRenderer", {})
            .get("content", {})
            .get("sectionListRenderer", {})
            .get("contents", [{}])[0]
            .get("itemSectionRenderer", {})
            .get("contents", [{}])[0]
            .get("aboutChannelRenderer", {})
            .get("metadata", {})
            .get("aboutChannelViewModel", {})
            .get("videoCountText")
        )
        number_videos = Convert.convert_number_videos(number_videos)
        return number_videos

    def get_subscriber(self):
        data = self.get_base_con()
        text_subscriber = (
            data[0]
            .get("showEngagementPanelEndpoint")
            .get("engagementPanel")
            .get("engagementPanelSectionListRenderer")
            .get("content")
            .get("sectionListRenderer")
            .get("contents")[0]
            .get("itemSectionRenderer")
            .get("contents")[0]
            .get("aboutChannelRenderer")
            .get("metadata")
            .get("aboutChannelViewModel")
            .get("subscriberCountText")
        )
        subscriber = Convert.convert_subscribers_to_int(text_subscriber)
        return subscriber

    def get_data_create(self):
        data = self.get_base_con()
        data_create = (
            data[0]
            .get("showEngagementPanelEndpoint", {})
            .get("engagementPanel", {})
            .get("engagementPanelSectionListRenderer", {})
            .get("content", {})
            .get("sectionListRenderer", {})
            .get("contents", [{}])[0]
            .get("itemSectionRenderer", {})
            .get("contents", [{}])[0]
            .get("aboutChannelRenderer", {})
            .get("metadata", {})
            .get("aboutChannelViewModel", {})
            .get("joinedDateText", {})
            .get("content")
        )
        data_create = Convert.convert_data_create(data_create)
        return data_create


    def get_description(self):
        data = self.get_base_con()
        text_description = (
            data[0]
            .get("showEngagementPanelEndpoint")
            .get("engagementPanel")
            .get("engagementPanelSectionListRenderer")
            .get("content")
            .get("sectionListRenderer")
            .get("contents")[0]
            .get("itemSectionRenderer")
            .get("contents")[0]
            .get("aboutChannelRenderer")
            .get("metadata")
            .get("aboutChannelViewModel")
            .get("description")
        )
        return text_description

    @property
    def object_channel(self):
        return self._object_channel


class YouTubeContent(RecipientYouTubeAbstract):
    def __init__(self, link, proxy=None, subtitles=None):
        self._proxy = proxy
        self._object_youtube = self.get_object_youtube(link, self._proxy)
        self.title = self._object_youtube.title
        self.likes = self.get_like_num(self._object_youtube)
        self.link = self._object_youtube.watch_url
        self.code = self._object_youtube.channel_id
        self.views = self._object_youtube.views
        self.system_id = self._object_youtube.video_id
        self.channel_url = self._object_youtube.channel_url
        self.publish_date = self._object_youtube.publish_date

        if subtitles:
            try:
                self.subtitles = self.get_subtitles(self._object_youtube)[1]
            except Exception:
                self.subtitles = None
        else:
            self.subtitles = None

    @staticmethod
    def get_object_youtube(link, proxy) -> YouTube:
        youtube = YouTube(link, proxies=proxy)
        return youtube

    @staticmethod
    def get_subtitles(youtube: YouTube):
        captions = youtube.captions
        if len(captions) == 0:
            return None

        caption = captions.get("en", False)

        try:
            caption = captions["en"]
            return caption

        except KeyError:
            return None

    @staticmethod
    def get_like_num(youtube: YouTube) -> bool | int:
        like_template = r"like this video along with (.*?) other people"
        text = str(youtube.initial_data)
        matches = re.findall(like_template, text, re.MULTILINE)
        if len(matches) >= 1:
            like_str = matches[0]
            return int(like_str.replace(",", ""))
        return False

    @classmethod
    def __str__(cls) -> str:
        return "video"

    @property
    def object_youtube(self):
        return self._object_youtube


class Convert:
    @staticmethod
    def convert_views_to_int(views_str: str) -> int:
        clean_str = views_str.replace(",", "").replace(" views", "").strip()
        return int(clean_str)

    @staticmethod
    def convert_subscribers_to_int(subscribers_str: str) -> int:
        clean_str = subscribers_str.replace(" subscribers", "").strip()

        if "K" in clean_str:
            return int(float(clean_str.replace("K", "")) * 1000)
        elif "M" in clean_str:
            return int(float(clean_str.replace("M", "")) * 1000000)
        else:
            return int(clean_str)

    @staticmethod
    def convert_number_videos(number_videos: str) -> int:
        return int(number_videos.split(' ')[0])

    @staticmethod
    def convert_data_create(data_create: str) -> datetime.date:
        date_part = data_create.replace("Joined ", "")
        joined_date = datetime.strptime(date_part, "%b %d, %Y").date()
        return joined_date