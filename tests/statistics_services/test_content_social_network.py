import dataclasses
import datetime

import pytest
from pytubefix import Channel

from foxycon import StatisticianSocNet
from foxycon.data_structures.analysis_type import ResultAnalytics
from foxycon.data_structures.statistician_type import YouTubeChannelsData


@pytest.fixture(scope="session")
def ob_channel():
    return Channel("https://www.youtube.com/@onlinegamercentral", "WEB", use_po_token=True)

@pytest.fixture(scope="session")
def object_statistics():
    return StatisticianSocNet()

@pytest.mark.statistics
def test_youtube_video_statistics_link_one(object_statistics, ob_channel):
    result_analyzer = object_statistics.get_data("https://www.youtube.com/@onlinegamercentral")
    assert Channel == type(result_analyzer.pytube_ob)

