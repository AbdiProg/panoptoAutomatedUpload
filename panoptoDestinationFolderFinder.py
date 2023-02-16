import json

import requests

#This Class provides 2 methods to find a destination over 2 layers of folders
class PanoptoFolderFinder:

    def __init__(self, meta_folder_id, oauth2):

        self.meta_folder_id = meta_folder_id
        self.oauth2 = oauth2
        self.requests_session = requests.Session()
        self.access_token = self.oauth2.get_access_token_authorization_code_grant()
        self.requests_session.headers.update({'Authorization': 'Bearer ' + self.access_token})

    def findSemesterFolderIDByString(self, semesterStr):
        resp = self.requests_session.get("https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/folders/{"
                                         "0}/children".format(self.meta_folder_id))
        responseJson = resp.json()


        for i in range (0, len(responseJson['Results'])):
            if responseJson['Results'][i]['Name'] == semesterStr:
                return responseJson['Results'][i]['Id']

    def findDestinationFolderByString(self, areaStr, semesterStr):
        resp = self.requests_session.get("https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/folders/{"
                                         "0}/children".format(self.findSemesterFolderIDByString(semesterStr)))
        responseJson = resp.json()

        for i in range(0, len(responseJson['Results'])):
            if responseJson['Results'][i]['Name'] == areaStr:
                return responseJson['Results'][i]['Id']