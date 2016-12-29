import os
from setuptools import setup

setup(
    name = "curl_parser",
    version = "1.0",
    author = "jinsub ahn",
    author_email = "jinniahn@gmail.com",
    description = ("parser module for curl command.")

    license = "MIT",
    keywords = "curl, network",
    url = "https://github.com/jinniahn/curl_parser",
    packages=['curl_parser'],
    install_requires=[
        'requests',
    ],    
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Networks"
    ]
)
