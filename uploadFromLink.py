#!python3
import requests
import os

from Tools.FileChooser import FileChooser
from UploadAndAuthentification_Algo.panopto_oauth2 import PanoptoOAuth2
from UploadAndAuthentification_Algo.panopto_uploaderConstruct import PanoptoUploader


class UploadFromOLW:
    client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

    client_secret = 'R9d8ao5bM+BjWWpzcANElnVUZz3jP1ixH4OUHOpn5c0='

    server = 'test-tu-darmstadt.cloud.panopto.eu'

    def __init__(self, requests_session):
        self.requests_session = requests_session
        self.oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', self.client_id, self.client_secret, True)

    def uploadSingleVideo(self, url, panoptoFolderID):
        panoptoUploader = PanoptoUploader(self.server, True, self.oauth2, "EinBeispielTitel",
                                          "EineBeispielBeschreibung")
        fileChooser = FileChooser(url,"https://olw-material.hrz.tu-darmstadt.de")
        print("Tfgdfgdfg",fileChooser.getOptimalVideoLink())
       # panoptoUploader.upload_video(fileChooser.getOptimalVideoLink(), "", panoptoFolderID)
