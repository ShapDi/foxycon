from foxycon.statistics_services.content_social_network import StatisticianSocNet
from foxycon.search_services.algorithms.algorithm_interface import SearchAlgorithm


class Search:
    def __init__(
        self,
        statistics_engine: StatisticianSocNet,
        search_algorithm: SearchAlgorithm,
    ):
        self._statistics_engine = statistics_engine
        self._search_algorithm = search_algorithm

    def create_search_generators(self):
        self._search_algorithm.init_statistic_engine(self._statistics_engine)
        return self._search_algorithm.get_search_generator()


class SearchBuilder:
    def __init__(self):
        self._list_search_algorithm: list[SearchAlgorithm] = []
        self._list_statistics_engine: list[StatisticianSocNet] = []

    def with_statistics_engine(self, statistics_engine: StatisticianSocNet):
        self._list_statistics_engine.append(statistics_engine)


    def with_search_algorithm(self, search_algorithm: SearchAlgorithm):
        self._list_search_algorithm.append(search_algorithm)

    def build(self):
        return [
            search_algorithm.init_statistic_engine(
                statistics_engine
            ).get_search_generator()()
            for search_algorithm in self._list_search_algorithm
            for statistics_engine in self._list_statistics_engine
        ]
