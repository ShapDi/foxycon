from foxycon import StatisticianSocNet
from foxycon.data_structures.statistician_type import ContentData
from foxycon.search_services.modules.search_youtube import ControllerParser


class Search:
    def __init__(
        self,
        proxy,
        telegram_accounts=None,
        subtitles=None,
        file_settings=None,
        search_algorithm=None,
        number_age=5,
    ):
        self._file_settings = file_settings
        self._search_algorithm = search_algorithm
        self._number_age = number_age
        self._statistician_object = StatisticianSocNet(
            proxy=proxy,
            file_settings=file_settings,
            telegram_accounts=telegram_accounts,
            subtitles=subtitles,
        )

    statistics_modules = {
        subclass().__str__(): subclass for subclass in ControllerParser.__subclasses__()
    }

    def get_parsers_controller(self, ob_stat: ContentData):
        return self.statistics_modules.get(ob_stat.analytics_obj.social_network)

    async def start_search(self, base_link):
        data = await self._statistician_object.get_data(base_link)
        print(data)
        return data
