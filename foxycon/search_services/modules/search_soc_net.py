from abc import ABC
from typing import Generator

from foxycon import StatisticianSocNet
from foxycon.search_services.modules.algorithm_search import Algorithm, AlgorithmRecommendation


class SearchStrategy(ABC):
    pass


class YoutubeSearch(SearchStrategy):
    def __init__(self, statistician_socnet_object, object_statistic):
        self._statistician_socnet_object: StatisticianSocNet = statistician_socnet_object
        self._object_statistic = object_statistic

    def get_algorithm(self)->Algorithm:
        pass

    async def create_generator(self)-> Generator:
        return await AlgorithmRecommendation(statistician_socnet_object = self._statistician_socnet_object,
                                       object_statistic=self._object_statistic).get_search_generator()

class InstagramSearch(SearchStrategy):
    pass

class TelegramSearch(SearchStrategy):
    pass