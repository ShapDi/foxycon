from abc import ABCMeta, abstractmethod
# from typing import Protocol, Union

from foxycon.statistics_services.content_social_network import StatisticianSocNet


class SearchAlgorithm(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def create_generator():
        pass

    @abstractmethod
    def init_statistic_engine(self, statistician_socnet_object: StatisticianSocNet):
        pass

    @abstractmethod
    def get_search_generator(self):
        pass
