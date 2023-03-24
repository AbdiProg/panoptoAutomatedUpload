import json

import requests

from CollectionHandler import urls, get_collection, get_lectureUnits, get_lecturers, get_areas
from Objects.Lecture import Lecture
from uploadFromOLWTools import UploadFromOLW

folder_id = 'ddce8d57-fcaa-402a-a1d1-afa900ec97d4'

client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

client_secret = 'WB1eyMbrDnP23QxOkhRR/8GXNJGhwxQhV+6aOMFooBw='


problematicCollections = []


def uploadLectureFromOLW():
    collectionIds = requests.get(f'{urls["api"]}{urls["collectionIds"]}')
    collectionJson = collectionIds.json()
    uploaderTools = UploadFromOLW(client_id, client_secret, folder_id)
    counter = 0
    for collection in collectionJson:
        tmpLecture = ""
        singleCollection = get_collection(collection['id'])
        print("Upload of Collection: ")
        print(json.dumps(singleCollection, indent=6, sort_keys=True))
        lectureName = singleCollection["name"]
        lectureDescription = singleCollection["description"]
        lectureLearningUnits = get_lectureUnits(singleCollection)
        lectureLecturers = get_lecturers(singleCollection)
        lectureAreas = get_areas(singleCollection)

        if "semesters" in singleCollection:
            print(True)
            lectureSemesterValue = singleCollection["semesters"][0]["value"]
            tmpLecture = Lecture(lectureName, lectureDescription, lectureLearningUnits, lectureLecturers, lectureAreas,
                                 lectureSemesterValue)
            uploaderTools.transferCollectionAsPlaylist(tmpLecture)
            counter += 1
        else:
            problematicCollections.append(singleCollection)

        if counter == 5:
            break


