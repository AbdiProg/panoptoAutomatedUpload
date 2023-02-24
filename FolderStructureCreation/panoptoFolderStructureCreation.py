import requests
import time
import folderNameExtraction



class FolderStructureCreation:

    # folder_names has to be a two-dimensional-array with "areas" in first place and "semesters" in second place.

    def __init__(self, panopto_metafolder_id, folder_names, oauth2):
        self.metaPanoptoFolderID = panopto_metafolder_id
        self.folderNames = folder_names
        self.oauth2 = oauth2

        self.requests_session = requests.Session()
        self.access_token = self.oauth2.get_access_token_authorization_code_grant()
        self.requests_session.headers.update({'Authorization': 'Bearer ' + self.access_token})

    def createFolderStructureInPanopto(self):

      print(self.folderNames)
      for folderAsSemesterName in self.folderNames[1]:

        payload = {'Name': folderAsSemesterName, 'Parent': self.metaPanoptoFolderID}
        resp = self.requests_session.post("https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/folders",
                                          payload)
        print(resp)
        time.sleep(10)
        responseJson = resp.json()
        print(responseJson)
        parentDirectoryID = responseJson['Id']

        for folderAsAreaName in self.folderNames[0]:
            payload2 = {'Name': folderAsAreaName, 'Parent': parentDirectoryID}
            resp2 = self.requests_session.post("https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/folders", payload2)
           # responseJson2 = resp2.json()