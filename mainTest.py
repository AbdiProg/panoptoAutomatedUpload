import requests

import uploadFromOLW
from CollectionHandler import get_collection, get_lectureUnits, get_informationOfCollection
from FolderStructureCreation import folderNameExtraction
from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from panoptoDestinationFolderFinder import PanoptoFolderFinder

# Upload-Test
from uploadFromLink import UploadFromLink

folder_id = 'ddce8d57-fcaa-402a-a1d1-afa900ec97d4'

client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

client_secret = 'WB1eyMbrDnP23QxOkhRR/8GXNJGhwxQhV+6aOMFooBw='

lecture = get_informationOfCollection(42)
lecture2 = get_informationOfCollection(43)

learningUnits = lecture.learningUnits
print(lecture.name)
print(lecture.areas[0].name)
print(lecture.semesterValue)
print(lecture2.name)
print(lecture2.areas[0].name)
print(lecture2.semesterValue)
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

# oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, True)

# panoptoFolderFinder = PanoptoFolderFinder("ddce8d57-fcaa-402a-a1d1-afa900ec97d4", oauth2)
# panopto_folder_id = panoptoFolderFinder.findDestinationFolderByString(lecture.areas[0].name, lecture.semesterValue)
# uploader = UploadFromOLW(oauth2)

# uploader = PanoptoUploader('test-tu-darmstadt.cloud.panopto.eu', True, oauth2, videoTitle, videoDescription)


olwUploader = uploadFromOLW.UploadFromOLW(client_id, client_secret)

olwUploader.transferCollectionAsPlaylist(lecture)
olwUploader.transferCollectionAsPlaylist(lecture2)

import csv

data_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
"""
data = open('companies.csv', 'a')

data.write("Test1")
data.write("\n") #else it appends directly to last line
data.write("Test2")
data.close()
"""
"""
with open('companies.csv', 'a') as file:
    write = csv.writer(file)
    for i in range(len(data_list[0])):
        write.writerow(data_list[0][i])

"""
# for pdf in pdfs: print(pdf.link)

# uploader.uploadVideoAndPdf(videoLink, pdfLink, "https://olw-material.hrz.tu-darmstadt.de", panopto_folder_id, learningUnits[1].name, "TestBeschreibung", videoLicense, pdfLicense)
