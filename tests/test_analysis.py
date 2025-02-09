from foxycon import ContentAnalyzer
from foxycon.data_structures.analysis_type import ResultAnalytics

ca = ContentAnalyzer()


def test_youtube_video_type_link_one():
    pass


def test_youtube_shorts():
    pass


def test_youtube_channel():
    pass


def test_instagram_page():
    pass


def test_instagram_reel():
    pass


def test_telegram_channel():
    assert ca.get_data("https://t.me/gregjgeek") == ResultAnalytics(
        url="https://t.me/gregjgeek",
        social_network="telegram",
        content_type="chat",
        code="gregjgeek",
    )


def test_telegram_post():
    assert ca.get_data("https://t.me/gregjgeek/957") == ResultAnalytics(
        url="https://t.me/gregjgeek/957",
        social_network="telegram",
        content_type="post",
        code="957",
    )
