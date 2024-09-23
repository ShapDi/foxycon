import inspect
import asyncio
from foxycon.analysis_services.сontent_analyzer import ContentAnalyzer
from foxycon.statistics_services.modules_youtube.statistics_social_network import StatisticianModuleStrategy


class StatisticianSocNet:
    statistics_modules = {subclass().__str__(): subclass for subclass in StatisticianModuleStrategy.__subclasses__()}

    def __init__(self, proxy=None, file_settings=None):
        self._proxy = proxy
        self._file_settings = file_settings
    @staticmethod
    def is_coroutine(func):
        return inspect.iscoroutinefunction(func)
    @staticmethod
    def get_basic_data(link):
        data = ContentAnalyzer().get_data(link)
        return data

    def get_data(self, link):
        data = self.get_basic_data(link)

        class_statistics = self.statistics_modules.get(f"{data.social_network}")
        if self.is_coroutine(class_statistics().get_data):
            data = asyncio.run(class_statistics().get_data(data))
        else:
            data = class_statistics().get_data(data)
        return data
