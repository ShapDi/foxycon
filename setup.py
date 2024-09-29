from setuptools import setup, find_packages

setup(
    name="foxycon",
    version="0.1.0",
    description="A package created to interact with various electrical networks based on other libraries.",
    author="ShapDi",
    author_email="shapranov.work@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "aiohttp==3.9.2",
        "aiosignal==1.3.1",
        "async-timeout==4.0.2",
        "attrs==22.2.0",
        "beautifulsoup4==4.11.2",
        "certifi==2024.8.30",
        "cffi==1.16.0",
        "charset-normalizer==2.1.1",
        "frozenlist==1.3.3",
        "idna==3.4",
        "instagram-auth==0.1.1",
        "multidict==6.0.4",
        "pycparser==2.21",
        "pycryptodomex==3.19.1",
        "PyNaCl==1.5.0",
        "pytube==15.0.0",
        "regex==2024.9.11",
        "requests==2.32.3",
        "soupsieve==2.3.2.post1",
        "typing_extensions==4.12.2",
        "urllib3==2.2.3",
        "yarl==1.8.2"
    ],
    extras_require={
        "instagram-reels": [
            "git+ssh://git@github.com/technology-department-mb/instastat.git@6ece09397445fc78790aeb6072cc72cd1fa5a343"
        ]
    },
    python_requires=">=3.10",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords=["electrical", "network", "analysis"],
)