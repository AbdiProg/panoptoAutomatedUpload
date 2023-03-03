from CollectionHandler import get_collection, get_lectureUnits, get_informationOfCollection
from FolderStructureCreation import folderNameExtraction
from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from panoptoDestinationFolderFinder import PanoptoFolderFinder

#Upload-Test
from uploadFromLink import UploadFromOLW

folder_id = 'ddce8d57-fcaa-402a-a1d1-afa900ec97d4'

client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

client_secret = 'PY9lSbz1OBtyUctzzDn02k2BrmzHj2gCtssr7+x2YL4='

lecture = get_informationOfCollection(78)

print(lecture.name)
learningUnits = lecture.learningUnits
print(learningUnits[1].name)
videoLink = learningUnits[1].resources[0].link
pdfLink =   learningUnits[1].resources[1].link
videoLicense = learningUnits[1].resources[0].license
pdfLicense = learningUnits[1].resources[1].license
print(videoLink)
print(pdfLink)
print(lecture.semesterValue)
print(lecture.areas[0].name)


oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, True)

panoptoFolderFinder = PanoptoFolderFinder("ddce8d57-fcaa-402a-a1d1-afa900ec97d4", oauth2)
panopto_folder_id = panoptoFolderFinder.findDestinationFolderByString(lecture.areas[0].name, lecture.semesterValue)
uploader = UploadFromOLW(oauth2)

uploader.uploadVideoAndPdf(videoLink, "", "https://olw-material.hrz.tu-darmstadt.de", panopto_folder_id, learningUnits[1].name, "TestBeschreibung", videoLicense, pdfLicense)
