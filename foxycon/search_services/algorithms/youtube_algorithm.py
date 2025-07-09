import json

from bs4 import BeautifulSoup
from regex import regex
from typing_extensions import override

from foxycon.data_structures.statistician_type import ContentData
from foxycon.search_services.algorithms.algorithm_interface import SearchAlgorithm
from foxycon.statistics_services.content_social_network import StatisticianSocNet


class YouTubeAlgorithmRecommendation(SearchAlgorithm):
    def __init__(self, link_start: str):
        self._link_start = link_start
        self._statistician_socnet_object = None
        self._parsing_object_controller = None
        self._list_link = None

    @override
    def init_statistic_engine(self, statistician_socnet_object: StatisticianSocNet):
        object_statistic = statistician_socnet_object.get_data(
            self._link_start, type_data="heavy"
        )
        self._statistician_socnet_object = statistician_socnet_object
        self._parsing_object_controller = ParsingObjectController(object_statistic)
        return self

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

    def get_soup_json_object(self, object_statistic):
        soup = BeautifulSoup(object_statistic.pytube_ob.watch_html, "html.parser")
        list_link = []
        try:
            for data in (
                self.extract_json(str(soup.html))[5]
                .get("playerOverlays")
                .get("playerOverlayRenderer")
                .get("endScreen")
                .get("watchNextEndScreenRenderer")
                .get("results")
            ):
                list_link.append(
                    f"https://www.youtube.com/watch?v={data.get('endScreenVideoRenderer').get('videoId')}"
                )

        except Exception:
            for data in (
                self.extract_json(str(soup.html))[6]
                .get("playerOverlays")
                .get("playerOverlayRenderer")
                .get("endScreen")
                .get("watchNextEndScreenRenderer")
                .get("results")
            ):
                list_link.append(
                    f"https://www.youtube.com/watch?v={data.get('endScreenVideoRenderer').get('videoId')}"
                )
        return list_link

    def get_list_object_statistic(self):
        list_object_statistic = []
        for link in self._list_link:
            object_statistic = self._statistician_socnet_object.get_data(
                link, type_data="heavy"
            )
            list_object_statistic.append(object_statistic)
        return list_object_statistic

    @override
    def create_generator(self):
        while True:
            list_object_statistic = (
                self._parsing_object_controller.search_statistics_object()
            )

            self._list_link = self.get_soup_json_object(list_object_statistic[0])
            list_object_statistic_data = self.get_list_object_statistic()
            list_object_statistic[1] = list_object_statistic_data
            self._parsing_object_controller.add_object_statistic(list_object_statistic)
            yield list_object_statistic

    @override
    def get_search_generator(self):
        return self.create_generator


class ParsingObjectController:
    def __init__(self, object_statistic: ContentData):
        self._search_structure: list[list] = [[object_statistic, None]]

    def get_object_statistic(self):
        return self.search_statistics_object()

    def search_statistics_object(self):
        if not self._search_structure:
            return None

        object_statistic_list = self._search_structure.pop(0)
        if object_statistic_list[1] is None:
            return object_statistic_list
        else:
            self._search_structure.append(object_statistic_list)
            self.changing_search_structure()
            return self.search_statistics_object()

    def add_object_statistic(self, object_statistic_list: list):
        self._search_structure.append(object_statistic_list)

    def changing_search_structure(self):
        new_search_structure = []

        for object_statistic_list in self._search_structure:
            for object_statistic in object_statistic_list[1]:
                new_search_structure.append([object_statistic, None])

        self._search_structure = new_search_structure
