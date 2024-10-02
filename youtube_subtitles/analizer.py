import srt

from pytubefix import YouTube
from foxycon.data_structures.country_type import Country


def try_get_subtitles(url: str, country: Country, one_line: bool = False) -> (bool, []):
    country_language_map = {
        Country.Russia: ['ru', 'a.ru'],
        Country.USA: ['en', 'a.en'],
        Country.India: ['hi', 'a.hi']
    }

    yt = YouTube(url)
    captions = yt.captions

    if len(captions) == 0:
        print('No subs')
        return False, []

    for code in country_language_map.get(country):
        caption = captions.get(code, False)

        if not caption:
            continue

        srt_captions = caption.generate_srt_captions()
        subtitles = ''

        for data in srt.parse(srt_captions):
            if not one_line:
                subtitles = f'{subtitles} {data.content}\n'
            else:
                subtitles = f'{subtitles} {data.content}'

        return True, subtitles

    print(f'No subs for {country.name}')
    return False, []
