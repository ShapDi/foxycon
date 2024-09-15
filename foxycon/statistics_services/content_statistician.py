import configparser

from foxycon.analysis_services.сontent_analyzer import ContentAnalyzer
from foxycon.statistics_services.statistics_modules import StatisticianModuleStrategy


class ContentStatistician:
    statistics_modules = {subclass().__str__(): subclass for subclass in StatisticianModuleStrategy.__subclasses__()}

    def __init__(self, proxy=None, file_settings=None):
        self._proxy = proxy
        self._file_settings = file_settings

    @staticmethod
    def get_basic_data(link):
        data = ContentAnalyzer().get_data(link)
        return data

    def get_data(self, link):
        data = self.get_basic_data(link)
