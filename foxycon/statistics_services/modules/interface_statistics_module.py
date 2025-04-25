from abc import ABC, abstractmethod


class StatisticianModuleStrategy(ABC):
    # def __init__(self, proxy=None, subtitles=None):
    #     self._proxy = proxy
    #     self._subtitles = subtitles

    @abstractmethod
    def get_data(self, object_sn, clients_handlers=None):
        pass

    @abstractmethod
    async def get_data_async(self, object_sn, clients_handlers=None):
        pass
