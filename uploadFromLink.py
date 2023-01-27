#!python3
import requests
import os

from Tools.FileChooser import FileChooser
from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from UploadAndAuthentificationPanopto_Algo.panopto_uploaderConstruct import PanoptoUploader


class UploadFromOLW:
    client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

    client_secret = 'R9d8ao5bM+BjWWpzcANElnVUZz3jP1ixH4OUHOpn5c0='

    server = 'test-tu-darmstadt.cloud.panopto.eu'

    def __init__(self, requests_session):
        self.requests_session = requests_session
        self.oauth2 = PanoptoOAuth2(self.server, self.client_id, self.client_secret, True)

    def uploadSingleVideo(self, url, main_url, panoptoFolderID, videoTitle, videoDescription):
        panoptoUploader = PanoptoUploader(self.server, True, self.oauth2, videoTitle,
                                          videoDescription)
        fileChooser = FileChooser(url, main_url)

        panoptoUploader.upload_video(fileChooser.getOptimalVideoLink(), "", panoptoFolderID)
