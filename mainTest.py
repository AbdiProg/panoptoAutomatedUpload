import folderNameExtraction
from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from panoptoDestinationFolderFinder import PanoptoFolderFinder
from panoptoFolderStructureCreation import FolderStructureCreation
from uploadFromLink import UploadFromOLW

url = "https://olw-material.hrz.tu-darmstadt.de/olw-konv-repository/material/68/d1/16/30/b9/21/11/e4/ae/75/00/50/56/bd/73/ad"
main_url = "https://olw-material.hrz.tu-darmstadt.de"
panoptoFolderID = "f8a51cec-09ed-4d07-9d32-af9700c5b342"
videoTitle = "Test"
videoDescription = "TestBeschreibung"

#uploader = UploadFromOLW("")
#uploader.uploadSingleVideo(url, main_url, panoptoFolderID, videoTitle, videoDescription)

client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

client_secret = 'S3Ndzc9QEU52PUuTxbctEz6H014LnLkIuaqmW/5xFWU='

oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, True)

identifiers = folderNameExtraction.returnArrayForFolderNameIdentification()

metaFolderID = "ddce8d57-fcaa-402a-a1d1-afa900ec97d4"


#folderStructure = FolderStructureCreation(metaFolderID, identifiers, oauth2)

#folderStructure.createFolderStructureInPanopto()

finder = PanoptoFolderFinder(metaFolderID,oauth2)


print(finder.findDestinationFolderByString("Philosophie","SoSe 2020"))