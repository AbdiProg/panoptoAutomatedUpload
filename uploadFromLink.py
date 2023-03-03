#!python3
import requests
import os

from Tools.FileChooser import FileChooser
from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from UploadAndAuthentificationPanopto_Algo.panopto_uploaderConstruct import PanoptoUploader


class UploadFromOLW:

    server = 'test-tu-darmstadt.cloud.panopto.eu'

    def __init__(self, oauth2):
        self.oauth2 = oauth2
        self.requests_session = requests.Session()
        self.access_token = oauth2.get_access_token_authorization_code_grant()
        self.requests_session.headers.update({'Authorization': 'Bearer ' + self.access_token})

    def uploadSingleVideo(self, url, main_url, panoptoFolderID, videoTitle, videoDescription):
        panoptoUploader = PanoptoUploader(self.server, True, self.oauth2, videoTitle,
                                          videoDescription)
        fileChooser = FileChooser(url, main_url)

        panoptoUploader.upload_video(fileChooser.getOptimalVideoLink(), "", panoptoFolderID)

    def uploadVideoAndPdf(self, videoLink, pdfLink, main_url, panoptoFolderID, videoTitle, videoDescription, videoLicense, pdfLicense):
        panoptoUploader = PanoptoUploader(self.server, True, self.oauth2, videoTitle,
                                          videoDescription)
        fileChooserPDF = ""
        fileChooserVideo = FileChooser(videoLink, main_url)
        if pdfLink != "":
            chooser = FileChooser(pdfLink, main_url)
            fileChooserPDF = chooser.getSlideLink()

        panoptoUploader.upload_video(fileChooserVideo.getOptimalVideoLink(), fileChooserPDF, panoptoFolderID)

