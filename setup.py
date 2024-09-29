from setuptools import setup, find_packages

setup(
    name='foxycon',
    version='0.1.0',
    description='A package created to interact with various electrical networks based on other libraries.',
    author='ShapDi',
    packages=['foxycon', 'foxycon.analysis_services', 'foxycon.analysis_services', 'foxycon.data_structures',
              'foxycon.statistics_services'],
    author_email='shapranov.work@gmail.com',
    url='git@github.com:ShapDi/foxycon.git',
    install_requires=[
        "aiohttp==3.9.2",
        "aiosignal==1.3.1",
        "cffi==1.16.0",
        "charset-normalizer==2.1.1",
        "frozenlist==1.3.3",
        "idna==3.7",
        "instagram-auth==0.1.1",
        "instagram-reels @ git+ssh://git@github.com/technology-department-mb/instastat.git@6ece09397445fc78790aeb6072cc72cd1fa5a343"
        "multidict==6.0.4",
        "pycparser==2.21",
        "pycryptodomex==3.19.1",
        "PyNaCl==1.5.0",
        "pytube==15.0.0",
        "regex==2024.9.11",
        "requests==2.32.3",
        "setuptools==68.2.0",
        "soupsieve==2.3.2.post1",
        "typing_extensions==4.12.2",
        "urllib3==2.2.3",
        "wheel==0.41.2",
        "yarl==1.8.2"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
