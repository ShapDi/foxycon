import urllib.parse
from typing import Type

from foxycon.analysis_services.analysis_modules import (
    AnalyzerModuleStrategy,
    YouTubeAnalyzer,
    InstagramAnalyzer,
    TelegramAnalyzer,
)
from foxycon.data_structures.analysis_type import ResultAnalytics


class ContentAnalyzer:
    @staticmethod
    def get_social_network_object(link: str) -> Type[AnalyzerModuleStrategy] | None:
        pars_link = urllib.parse.urlparse(link)
        match pars_link.netloc:
            case "youtu.be":
                return YouTubeAnalyzer
            case "youtube.com":
                return YouTubeAnalyzer
            case "www.youtube.com":
                return YouTubeAnalyzer
            case "www.instagram.com":
                return InstagramAnalyzer
            case "t.me":
                return TelegramAnalyzer
        return None

    def get_data(self, link) -> ResultAnalytics | None:
        analysis_modules = self.get_social_network_object(link)
        if analysis_modules is not None:
            data_analysis = analysis_modules().get_data(link)
            result = ResultAnalytics(
                url=data_analysis.get("clean_link"),
                social_network=data_analysis.get("social_network"),
                content_type=data_analysis.get("type_content"),
                code=data_analysis.get("code"),
            )
            return result
        else:
            return None
