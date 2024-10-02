from setuptools import setup, find_packages

setup(
    name='foxycon',
    version='0.1.0',
    description='A package created to interact with various electrical networks based on other libraries.',
    author='ShapDi',
    packages=['foxycon', 'foxycon.analysis_services', 'foxycon.analysis_services', 'foxycon.data_structures',
              'foxycon.statistics_services', 'foxycon.utils', 'foxycon.statistics_services.modules'],
    author_email='shapranov.work@gmail.com',
    url='git@github.com:ShapDi/foxycon.git',
    install_requires=[
        "pytubefix==7.1.3",
        "instagram-reels @ git+ssh://git@github.com/technology-department-mb/instastat.git@6ece09397445fc78790aeb6072cc72cd1fa5a343"
        'regex==2024.9.11',
        'requests==2.32.3',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
