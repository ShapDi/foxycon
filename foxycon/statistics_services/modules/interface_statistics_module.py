from abc import ABC, abstractmethod


class StatisticianModuleStrategy(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    async def get_data_async(self):
        pass
