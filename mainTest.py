from CollectionHandler import get_collection, get_lectureUnits, get_informationOfCollection
from FolderStructureCreation import folderNameExtraction
from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from panoptoDestinationFolderFinder import PanoptoFolderFinder

#Upload-Test
from uploadFromLink import UploadFromLink
from uploadFromOLW import uploadSingleLearningUnit

folder_id = 'ddce8d57-fcaa-402a-a1d1-afa900ec97d4'

client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

client_secret = 'WB1eyMbrDnP23QxOkhRR/8GXNJGhwxQhV+6aOMFooBw='

lecture = get_informationOfCollection(42)
learningUnits = lecture.learningUnits
"""
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
"""

#oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, True)

#panoptoFolderFinder = PanoptoFolderFinder("ddce8d57-fcaa-402a-a1d1-afa900ec97d4", oauth2)
#panopto_folder_id = panoptoFolderFinder.findDestinationFolderByString(lecture.areas[0].name, lecture.semesterValue)
#uploader = UploadFromOLW(oauth2)


uploadSingleLearningUnit(learningUnits[1])

#for pdf in pdfs: print(pdf.link)

#uploader.uploadVideoAndPdf(videoLink, pdfLink, "https://olw-material.hrz.tu-darmstadt.de", panopto_folder_id, learningUnits[1].name, "TestBeschreibung", videoLicense, pdfLicense)
