# from foxycon.search_services import DataGoogleSearch, LanguageGoogle, TimeGoogle, CountryGoogle
# data = DataGoogleSearch(language = 'lang_e', country = 'CA', period = 'year')
import asyncio
from typing import Annotated

Annotated

from foxycon import StatisticianSocNet
# Нужно найти воронки по гео чили перу Аргентина Колумбия Бангладеш
# Суть рекламы будет «заработай со мной»
# И дальше реклама ведет в телеграмм канал , aviator
#
# # serch = ['aviator', 'make money with me', 'ganhar dinheiro comigo', 'ganar dinero conmigo']
# # data = []
# #
# # for i in serch:
# #     data_fb = DataFBAdsLib(text = i, country = CountryAds.Argentina).get_data()
# #     data = data + data_fb
# #     data_fb = DataFBAdsLib(text = i, country = CountryAds.Brazi).get_data()
# #     data = data + data_fb
# #     data_fb = DataFBAdsLib(text = i, country = CountryAds.Peru).get_data()
# #     data = data + data_fb
# #
# # AutoTablePacker(name = 'table', path = 'C:\git\FoxyCon', data = data).get_facebook_ads()
# #
#
#
# ip_list = [
#     'http://zjMKKB:3ru9Pn@185.39.149.135:8000',
#     'http://zjMKKB:3ru9Pn@91.216.59.86:8000'
# ]
# dad = DataGoogleSearch(language = LanguageGoogle.english.value,
#                        country = CountryGoogle.india.value,
#                        period = TimeGoogle.week.value,
#                        num = 400,
#                        type_search = 'standard')
#
# reqvest = ['mostbet','1xbet', 'parimatch']
#
# for i in reqvest:
#     print(dad.get_instagram('mostbet'))


from foxycon.analysis_services.сontent_analyzer import ContentAnalyzer

proxy = [
    "http://shapdi:8b3yGiQBjy1D@93.183.125.176:3128",
    "http://shapdi2:BVZzY5xENsN1@194.246.82.177:3128",
]
#
ca = ContentAnalyzer()

# print(ca.get_data("https://t.me/Blazzerfox/6708"))
print(ca.get_data.__code__)

# print(ca.get_data("fasfdszfs"))
# print(ca.get_data("https://github.com/technology-department-mb/bot_papich"))
# print(ca.get_data("https://www.instagram.com/blyea_u/"))
# print(ca.get_data("https://youtu.be/dMPPMmUrYQM?si=_uGQVE6wtTXnVULv&t=32"))
# print(ca.get_data("https://youtu.be/GhXMLM7vUJI2"))
# print(ca.get_data("https://drive.google.com/file/d/1-RlcfHoyOnnxVa-aMks7nq-ex3Cy5lCs/view?usp=sharing"))
# print(ca.get_data("fasfdszfs"))
# print(ca.get_data("https://github.com/technology-department-mb/bot_papich"))
# print(ca.get_data("https://www.instagram.com/blyea_u/"))
# print(ca.get_data("https://www.instagram.com/reel/C9NSNb5ow03/?igsh=a29uNGk0eTdta3Fw"))
#
# print(ca.get_data("https://www.instagram.com/p/C9HMrwooyGW/ "))
# print(ca.get_data("https://www.instagram.com/prikol.pedro/"))
# print(ca.get_data("https://www.instagram.com/papich_legenda"))
# print(ca.get_data("https://www.instagram.com/reel/C9kE36uxz_v/?igsh=YXF2NXVmaG9pOWZt"))
# print(ca.get_data("https://www.youtube.com/channel/UC5C088kVlcF5ras7cBbdWxw"))
# print(ca.get_data("https://www.youtube.com/shorts/J-m4POZFGyM"))
# print(ca.get_data("https://www.youtube.com/@AgnamoN"))
#
# # print(ca.get_data("https://www.tiktok.com/@univer_serial1?_t=8oe1uJ7kZQo&_r=1 https://www.tiktok.com/t/ZTNbRpGhg/"))
# # print(ca.get_data("https://www.tiktok.com/@yourfavrum/video/7394549234214636807?_t=8oe1rB7TXRR&_r=1"))
# print(ca.get_data("https://www.youtube.com/watch?v=yydTXyC9StM&t=139s"))
# print(ca.get_data("https://www.youtube.com/@basitrind"))
# print(ca.get_data("https://www.youtube.com/channel/UC5C088kVlcF5ras7cBbdWxw"))
# print(ca.get_data("https://www.youtube.com/watch?v=M4HCrPSU0C0?start=92.40&end=96.30"))
#
# ssn = StatisticianSocNet(proxy=proxy, subtitles=True)


# print(asyncio.run(ssn.get_data('https://www.youtube.com/@basitrind')))
# print(ssn.get_data('https://www.youtube.com/@basitrind'))
# print(ca.get_data("https://www.youtube.com/watch?v=ELjqloF-P2M"))
# print(ssn.get_data('https://www.youtube.com/watch?v=ELjqloF-P2M'))

# print(ca.get_data("https://www.youtube.com/watch?v=6rjaNgA8Okc&list=RDQO0IWTDp96c&index=3"))
# print(ssn.get_data('https://www.youtube.com/watch?v=6rjaNgA8Okc&list=RDQO0IWTDp96c&index=3'))


#
# print(asyncio.runssn.get_data('https://www.instagram.com/reels/DAh0fmFos5w/'))
# print(ssn.get_data("https://www.youtube.com/channel/UC5C088kVlcF5ras7cBbdWxw"))
print(ca.get_data("https://youtu.be/WikF9bhMQLs?si=pTM2n2vccZItmSnI&t=113"))


async def main_corut():
    ssn = StatisticianSocNet(
        proxy=proxy,
        telegram_account=[
            {
                "api_id": 22810893,
                "api_hash": "cf16ee6136d10d41a98e8398fa42e6d8",
                "session": "1ApWapzMBu1q0fH1WHPUFiMhb4UKZd1KO4ACWhOypt4mmbKWKOBsgI-9nuWcen9humyKg_L99HPTPVrpVF7XnY3hBRrvr8FG0bi8_wvIoXwvsDH0Eg-8KNS07RYPq0ehsXm5ZaZ_Z4MWYB53mc0nrgI2OGWnXAZNUARpUkB6DG5QefLclZAGvmZ2rxx2Pdy3x8pbeB8pdFth6mFYzroXo7XFfZzyDn6x6x9TnhUm8X9Sx8imaSgOArJ0sckP3yPE8xshNFv-OFGiGLTUw5a80y3xP6qanRh6jISXq7ZYkOeGsNNwktP1VVH2-Pa4nTAIXVf2TWwyjfI8_Vx-r77V14oG0r6ngh6M=",
            }
        ],
    )

    #
    data = await ssn.get_data("https://t.me/gregjgeek/958")
    # data = await ssn.get_data("https://t.me/-4767368554/6708")
    #     print(data)
    # https: // t.me / 4767368554 / 6708
    # "
    # data = await ssn.get_data("https://www.youtube.com/watch?v=WikF9bhMQLs&t=113s")
    print(data)
    # data = await ssn.get_data("https://www.youtube.com/shorts/S8FjjoLTwYo")
    # print(data)
    # data = await ssn.get_data("https://www.youtube.com/watch?v=YgsmFeawp-E")
    # print(data)
    #
    #
    # data = await ssn.get_data('https://www.youtube.com/watch?v=yydTXyC9StM&t=139s')
    # print(data)
    # data = await ssn.get_data('https://www.instagram.com/reels/DAh0fmFos5w/')
    # print(data)


# search = await Search(proxy=proxy, subtitles=True).search('https://www.youtube.com/watch?v=yydTXyC9StM&t=139s')
# async for i in search():
#     print(i)
# print(search)


asyncio.run(main_corut())

# print(ssn.get_data('https://www.instagram.com/reel/C9NSNb5ow03/?igsh=a29uNGk0eTdta3Fw'))
# print(ssn.get_data("https://www.youtube.com/channel/UC5C088kVlcF5ras7cBbdWxw"))
#
#
