import urllib.parse

import phub

from foxycon.data_structures.statistician_type import PornHabModelData, PornHabVideoData
from foxycon.statistics_services.modules.interface_statistics_module import (
    StatisticianModuleStrategy,
)


class PornHabVideo(StatisticianModuleStrategy):
    def __init__(self, link, analytics_obj):
        self._link = link
        self._analytics_obj = (analytics_obj,)

    def get_data(self):
        client = phub.Client()
        video = client.get(self._link)
        return PornHabVideoData(
            system_id=video.id,
            channel_id=video.author.name,
            title=video.title,
            likes=video.likes.up,
            dislikes=video.likes.down,
            views=video.views,
            duration=video.duration,
            channel_url=f"https://www.pornhub.com/{video.author.url}",
            publish_date=video.date,
            analytics_obj=self._analytics_obj,
        )

    async def get_data_async(self):
        client = phub.Client()
        video = client.get(self._link)
        return PornHabVideoData()
