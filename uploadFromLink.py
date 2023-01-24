#!python3
import requests
import os

class UploadFromLink:

    def __init__(self, requests_session, panoptoUploader, oauth2):

        self.requests_session = requests_session
        self.panoptoUploader = panoptoUploader
        self.oauth2 = oauth2


     def upload(self, url, panoptoFolderID):
        requests.get(url)
