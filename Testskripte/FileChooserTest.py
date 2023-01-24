import requests
import os
from bs4 import BeautifulSoup

from UploadAndAuthentification_Algo.panopto_uploaderConstruct import PanoptoUploader

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


