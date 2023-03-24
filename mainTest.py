import requests

import uploadFromOLWTools
from CollectionHandler import get_collection, get_lectureUnits, get_informationOfCollection, \
    get_informationOfAllCollections
from FolderStructureCreation import folderNameExtraction
from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from panoptoDestinationFolderFinder import PanoptoFolderFinder

# Upload-Test
from uploadCollectionFromOLW import uploadLectureFromOLW
from uploadFromLink import UploadFromLink



uploadLectureFromOLW()


