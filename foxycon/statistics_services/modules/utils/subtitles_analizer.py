import srt

from pytubefix import YouTube


def try_get_subtitles(youtube: YouTube, one_line: bool = False) -> (bool, []):
    languages = ["ru", "a.ru", "hi", "te", "a.hi", "a.te", "en", "a.en"]

    captions = youtube.captions

    if len(captions) == 0:
        return False, []

    for language in languages:
        caption = captions.get(language, False)

        if not caption:
            continue

        srt_captions = caption.generate_srt_captions()
        subtitles = ""

        for data in srt.parse(srt_captions):
            if not one_line:
                subtitles = f"{subtitles} {data.content}\n"
            else:
                subtitles = f"{subtitles} {data.content}"

        return True, subtitles

    return False, []
