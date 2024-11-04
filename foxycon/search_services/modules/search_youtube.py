# Для функционирования системы как ноды поиска необходисо учесть обход блокировок при поиске
# с целью этого должны быть введены следующие системы.
# 1. Подержка прокси
# 2. Задержка перед каждым запросом
# 3. Системы управления прокси заблокироваными при блокервки
# 4. Задержка между поколениями
# 5. Задержка при выбытии 50 %  прокси

# Для очистки ссылок вести пареметров
# 1. Убирать дубликаты каналов
# 2. Убирать дубликаты видео (Обязательно)

from regex import regex
from bs4 import BeautifulSoup
import json
from abc import ABC, abstractmethod


class ControllerParser(ABC):
    @abstractmethod
    def get_parsers(self):
        pass

    @abstractmethod
    def get_data(self):
        pass


class ControllerParserYoutube(ControllerParser):
    pass


class ControllerParserInstagram(ControllerParser):
    pass


class Tree(ABC):
    pass


class Age(ABC):
    pass


class SearchInternalAlgorithm(ABC):
    def __init__(self, obj_youtube):
        self._obj_youtube = obj_youtube

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

    @staticmethod
    def get_soup_obj(youtube):
        soup = BeautifulSoup(youtube.watch_html, "html.parser")
        return soup

    def get_link(self):
        soup = self.get_soup_obj(self._obj_youtube)
        json = self.extract_json(str(soup.html))
        try:
            json = (
                json[6]
                .get("playerOverlays")
                .get("playerOverlayRenderer")
                .get("endScreen")
                .get("watchNextEndScreenRenderer")
                .get("results")
            )
        except:
            json = (
                json[5]
                .get("playerOverlays")
                .get("playerOverlayRenderer")
                .get("endScreen")
                .get("watchNextEndScreenRenderer")
                .get("results")
            )

        for data in json:
            yield (
                f'https://www.youtube.com/watch?v={data.get("endScreenVideoRenderer").get("videoId")}'
            )


class SearchYoutube:
    pass
