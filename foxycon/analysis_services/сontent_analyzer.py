import re

from foxycon.analysis_services.analysis_modules import AnalyzerModuleStrategy
from foxycon.data_structures.analysis_type import SocialNetwork, ResultAnalytics


class ContentAnalyzer:
    analysis_modules = {subclass().__str__(): subclass for subclass in AnalyzerModuleStrategy.__subclasses__()}

    @classmethod
    def get_social_network(cls, link: str) -> str | None:
        if not isinstance(link, str) or not re.match(r'https?://', link):
            return None

        for network in SocialNetwork:
            if re.search(network.value, link):
                return network.name.lower()

        return None

    def get_data(self, link):
        social_network = self.get_social_network(link)
        if social_network is not None:
            class_analysis = self.analysis_modules.get(social_network)

            data = class_analysis().get_data(link)
            result = ResultAnalytics(link=data.get("clean_link"),
                                     social_network=social_network,
                                     content_type=data.get("type_content"),
                                     code=data.get("code"))
            print(result)
            return result
        else:
            return None
