# from foxycon.search_services import DataGoogleSearch, LanguageGoogle, TimeGoogle, CountryGoogle
from foxycon import StatisticianSocNet
# data = DataGoogleSearch(language = 'lang_e', country = 'CA', period = 'year')

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

ca = ContentAnalyzer()

print(ca.get_data("fasfdszfs"))
print(ca.get_data("https://github.com/technology-department-mb/bot_papich"))
print(ca.get_data("https://www.instagram.com/blyea_u/"))
print(ca.get_data("https://www.instagram.com/reel/C9NSNb5ow03/?igsh=a29uNGk0eTdta3Fw"))

print(ca.get_data("fasfdszfs"))
print(ca.get_data("https://github.com/technology-department-mb/bot_papich"))
print(ca.get_data("https://www.instagram.com/blyea_u/"))
print(ca.get_data("https://www.instagram.com/reel/C9NSNb5ow03/?igsh=a29uNGk0eTdta3Fw"))

print(ca.get_data("https://www.instagram.com/p/C9HMrwooyGW/ "))
print(ca.get_data("https://www.instagram.com/prikol.pedro/"))
print(ca.get_data("https://www.instagram.com/papich_legenda"))
print(ca.get_data("https://www.instagram.com/reel/C9kE36uxz_v/?igsh=YXF2NXVmaG9pOWZt"))
print(ca.get_data("https://www.tiktok.com/@univer_serial1?_t=8oe1uJ7kZQo&_r=1 https://www.tiktok.com/t/ZTNbRpGhg/"))
print(ca.get_data("https://www.tiktok.com/@yourfavrum/video/7394549234214636807?_t=8oe1rB7TXRR&_r=1"))
print(ca.get_data("https://www.youtube.com/watch?v=yydTXyC9StM&t=139s"))
print(ca.get_data("https://www.youtube.com/@basitrind"))


print(StatisticianSocNet().get_data('https://www.youtube.com/@basitrind'))
print(StatisticianSocNet().get_data('https://www.youtube.com/watch?v=yydTXyC9StM&t=139s'))

print(StatisticianSocNet().get_data('https://www.instagram.com/reel/C9NSNb5ow03/?igsh=a29uNGk0eTdta3Fw'))
