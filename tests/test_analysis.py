from foxycon import ContentAnalyzer
from foxycon.data_structures.analysis_type import ResultAnalytics

ca = ContentAnalyzer()


def test_youtube_video_type_link_one():
    assert ca.get_data(
        "https://youtu.be/dMPPMmUrYQM?si=_uGQVE6wtTXnVULv&t=32"
    ) == ResultAnalytics(
        url="https://youtube.com/watch?v=dMPPMmUrYQM",
        social_network="youtube",
        content_type="video",
        code="dMPPMmUrYQM",
    )


def test_youtube_video_type_link_two():
    assert ca.get_data("https://youtu.be/GhXMLM7vUJI2") == ResultAnalytics(
        url="https://youtube.com/watch?v=GhXMLM7vUJI2",
        social_network="youtube",
        content_type="video",
        code="GhXMLM7vUJI2",
    )


def test_youtube_video_type_link_thee():
    assert ca.get_data("https://www.youtube.com/shorts/J-m4POZFGyM") == ResultAnalytics(
        url="https://youtube.com/watch?v=J-m4POZFGyM",
        social_network="youtube",
        content_type="shorts",
        code="J-m4POZFGyM",
    )


def test_youtube_video_type_link_four():
    assert ca.get_data(
        "https://www.youtube.com/watch?v=M4HCrPSU0C0?start=92.40&end=96.30"
    ) == ResultAnalytics(
        url="https://youtube.com/watch?v=M4HCrPSU0C0",
        social_network="youtube",
        content_type="video",
        code="M4HCrPSU0C0",
    )


def test_youtube_shorts():
    assert ca.get_data("https://www.youtube.com/shorts/J-m4POZFGyM") == ResultAnalytics(
        url="https://youtube.com/watch?v=J-m4POZFGyM",
        social_network="youtube",
        content_type="shorts",
        code="J-m4POZFGyM",
    )


def test_youtube_channel_type_link_one():
    assert ca.get_data("https://www.youtube.com/@AgnamoN") == ResultAnalytics(
        url="https://www.youtube.com/@AgnamoN",
        social_network="youtube",
        content_type="channel",
        code="AgnamoN",
    )


def test_youtube_channel_type_link_two():
    assert ca.get_data(
        "https://www.youtube.com/channel/UC5C088kVlcF5ras7cBbdWxw"
    ) == ResultAnalytics(
        url="https://www.youtube.com/channel/UC5C088kVlcF5ras7cBbdWxw",
        social_network="youtube",
        content_type="channel",
        code="UC5C088kVlcF5ras7cBbdWxw",
    )


def test_instagram_page():
    assert ca.get_data("https://www.instagram.com/prikol.pedro/") == ResultAnalytics(
        url="https://www.instagram.com/prikol.pedro/",
        social_network="instagram",
        content_type="page",
        code="prikol.pedro",
    )


def test_instagram_post():
    assert ca.get_data("https://www.instagram.com/p/C9HMrwooyGW/") == ResultAnalytics(
        url="https://www.instagram.com/p/C9HMrwooyGW/",
        social_network="instagram",
        content_type="post",
        code="C9HMrwooyGW",
    )


def test_instagram_reel():
    assert ca.get_data(
        "https://www.instagram.com/reel/C9kE36uxz_v/?igsh=YXF2NXVmaG9pOWZt"
    ) == ResultAnalytics(
        url="https://www.instagram.com/reel/C9kE36uxz_v/",
        social_network="instagram",
        content_type="reel",
        code="C9kE36uxz_v",
    )


def test_google_drive():
    assert ca.get_data(
        "https://drive.google.com/file/d/1-RlcfHoyOnnxVa-aMks7nq-ex3Cy5lCs/view?usp=sharing"
    ) == ResultAnalytics(
        url="https://drive.google.com/file/d/1-RlcfHoyOnnxVa-aMks7nq-ex3Cy5lCs/view",
        social_network="google_drive",
        content_type="meet",
        code="1-RlcfHoyOnnxVa-aMks7nq-ex3Cy5lCs",
    )


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
