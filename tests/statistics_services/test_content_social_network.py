import dataclasses
import datetime

import pytest
from pytubefix import Channel

from foxycon import StatisticianSocNet
from foxycon.data_structures.analysis_type import ResultAnalytics
from foxycon.data_structures.statistician_type import (
    YouTubeChannelsData,
    CoreYouTubeChannelsData,
)


@pytest.fixture(scope="session")
def ob_channel():
    return Channel(
        "https://www.youtube.com/@onlinegamercentral", "WEB", use_po_token=True
    )


@pytest.fixture(scope="session")
def object_statistics():
    return StatisticianSocNet()


@pytest.mark.statistics
def test_youtube_video_statistics_link_one(object_statistics, ob_channel):
    result_analyzer = object_statistics.get_data(
        "https://www.youtube.com/@onlinegamercentral"
    )
    test_youtube_ob = CoreYouTubeChannelsData(
        analytics_obj=ResultAnalytics(
            url="https://www.youtube.com/@onlinegamercentral",
            social_network="youtube",
            content_type="channel",
            code="onlinegamercentral",
        ),
        channel_id="UC1CchA0SjApw4T-AYkN7ytg",
        name="IGM",
        link="https://www.youtube.com/@onlinegamercentral",
        description="Официальный канал сообщества IGM в VK.\n\nМы делаем контент для всех, кто интересуется игровой индустрией.\n\nНесколько раз в неделю мы выпускаем самые разные ролики о видеоиграх: взлёт, эволюции и смерть серии игр... рецензии и много другого.\n\nПодписывайтесь на канал, чтобы не пропустить видео от IGM. Скоро услышимся!\n\nПо вопросам рекламы: \nadv@igm.gg\n\nПо вопросам сотрудничества:\nTodd@igm.gg\n\nРегистрация в перечне владельцев соцсетей: https://knd.gov.ru/license?id=675ad347e9320a200a8e4da7&registryType=bloggersPermission\n",
        country="Russia",
        view_count=859542439,
        subscriber=2840000,
        number_videos=5824,
        data_create=datetime.date(2013, 9, 19),
    )
    result_analyzer_core_data = CoreYouTubeChannelsData(
        analytics_obj=result_analyzer.analytics_obj,
        channel_id=result_analyzer.channel_id,
        name=result_analyzer.name,
        link=result_analyzer.link,
        description=result_analyzer.description,
        country=result_analyzer.country,
        view_count=result_analyzer.view_count,
        subscriber=result_analyzer.subscriber,
        number_videos=result_analyzer.number_videos,
        data_create=result_analyzer.data_create,
    )
    assert Channel == type(result_analyzer.pytube_ob)
    assert test_youtube_ob == result_analyzer_core_data


@pytest.mark.statistics
def test_youtube_video_statistics_link_one(object_statistics, ob_channel):
    result_analyzer = object_statistics.get_data(
        "https://www.youtube.com/@onlinegamercentral"
    )
    test_youtube_ob = CoreYouTubeChannelsData(
        analytics_obj=ResultAnalytics(
            url="https://www.youtube.com/@onlinegamercentral",
            social_network="youtube",
            content_type="channel",
            code="onlinegamercentral",
        ),
        channel_id="UC1CchA0SjApw4T-AYkN7ytg",
        name="IGM",
        link="https://www.youtube.com/@onlinegamercentral",
        description="Официальный канал сообщества IGM в VK.\n\nМы делаем контент для всех, кто интересуется игровой индустрией.\n\nНесколько раз в неделю мы выпускаем самые разные ролики о видеоиграх: взлёт, эволюции и смерть серии игр... рецензии и много другого.\n\nПодписывайтесь на канал, чтобы не пропустить видео от IGM. Скоро услышимся!\n\nПо вопросам рекламы: \nadv@igm.gg\n\nПо вопросам сотрудничества:\nTodd@igm.gg\n\nРегистрация в перечне владельцев соцсетей: https://knd.gov.ru/license?id=675ad347e9320a200a8e4da7&registryType=bloggersPermission\n",
        country="Russia",
        view_count=859542439,
        subscriber=2840000,
        number_videos=5824,
        data_create=datetime.date(2013, 9, 19),
    )
    result_analyzer_core_data = CoreYouTubeChannelsData(
        analytics_obj=result_analyzer.analytics_obj,
        channel_id=result_analyzer.channel_id,
        name=result_analyzer.name,
        link=result_analyzer.link,
        description=result_analyzer.description,
        country=result_analyzer.country,
        view_count=result_analyzer.view_count,
        subscriber=result_analyzer.subscriber,
        number_videos=result_analyzer.number_videos,
        data_create=result_analyzer.data_create,
    )
    assert Channel == type(result_analyzer.pytube_ob)
    assert test_youtube_ob == result_analyzer_core_data
