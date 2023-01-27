import requests
import os
from bs4 import BeautifulSoup

from UploadAndAuthentificationPanopto_Algo.panopto_uploaderConstruct import PanoptoUploader

import requests
import os
from bs4 import BeautifulSoup


class FileChooser:
    videoEndings = [
        "3.mp4",
        "9.mp4",
        "2.mp4",
        "1.mp4",
        "4.mp4",
        "205.webm",
        "106.webm",
        "105.webm"
    ]

    slideEndings = [
        ""
    ]

    def __init__(self, url, main_url):
        self.main_url = main_url
        self.url = url
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text, 'html.parser')
        self.parent = [node.get('href') for node in self.soup.find_all('a')]
    # This method searches for the optimal video with the best quality provided by the website
    # The website is called with an url
    def getOptimalVideoLink(self):
        for ending in self.videoEndings:
            for link in self.parent:
                linkStr = str(link)
                if linkStr.__contains__(ending):
                    return self.main_url+link


# def getSlidesLink(self):

"""
url = "https://olw-material.hrz.tu-darmstadt.de/olw-konv-repository/material/e6/1d/69/70/01/e1/11/ed/87/6c/00/50/56/bd/73/ae"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
parent = [url + node.get('href') for node in soup.find_all('a')]

endings = [
    "3.mp4",
    "9.mp4",
    "2.mp4",
    "1.mp4",
    "4.mp4",
    "205.webm",
    "106.webm",
    "105.webm"
]


def findWithEnding(linkArray):
    for ending in endings:
        for link in linkArray:
            linkStr = str(link)
            if linkStr.__contains__(ending):
                return link
"""
