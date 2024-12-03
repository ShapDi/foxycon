import urllib.parse
from typing import Type

from foxycon.analysis_services.analysis_modules import AnalyzerModuleStrategy, YouTubeAnalyzer, GoogleDriveAnalyzer, \
    InstagramAnalyzer
from foxycon.data_structures.analysis_type import SocialNetwork, ResultAnalytics


class ContentAnalyzer:
    analysis_modules = {
        subclass().__str__(): subclass
        for subclass in AnalyzerModuleStrategy.__subclasses__()
    }

    @staticmethod
    def get_social_network_object(link: str) -> Type[AnalyzerModuleStrategy] | None:
        pars_link = urllib.parse.urlparse(link)
        match pars_link.netloc:
            case 'youtu.be':
                return YouTubeAnalyzer
            case 'www.youtube.com':
                return YouTubeAnalyzer
            case 'www.instagram.com':
                return InstagramAnalyzer
            case 'drive.google.com':
                return GoogleDriveAnalyzer
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
