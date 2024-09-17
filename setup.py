from setuptools import setup, find_packages

setup(
    name='foxycon',
    version='0.1.0',
    description='A package created to interact with various electrical networks based on other libraries.',
    author='ShapDi',
    packages=['foxycon', 'foxycon.analysis_services', 'foxycon.analysis_services', 'foxycon.data_structures', 'foxycon.statistics_services'],
    author_email='shapranov.work@gmail.com',
    url='git@github.com:ShapDi/FoxyCon.git',
    install_requires=[
        'pytube==15.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
