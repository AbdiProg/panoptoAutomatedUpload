import csv
import json

import requests

from CollectionHandler import urls, get_collection, get_lectureUnits, get_lecturers, get_areas
from Objects.Lecture import Lecture
from uploadFromOLWTools import UploadFromOLW

folder_id = 'ddce8d57-fcaa-402a-a1d1-afa900ec97d4'

client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

client_secret = 'WB1eyMbrDnP23QxOkhRR/8GXNJGhwxQhV+6aOMFooBw='

problematicCollections = []

lecturerContingent = 10

alreadyUploaded = 82

def writeProblematicCollectionIntoCSV(lecture):
    lecturersString = ";"
    counter = 0
    for lecturer in lecture.lecturers:
        """lecturersString = lecturersString + str(lecturer.id) + " " +lecturer.title + " " + lecturer.fullName + ","""

        if counter == len(lecture.lecturers) - 1:
            lecturersString = lecturersString + str(lecturer.id) + ";"
        else:
            lecturersString = lecturersString + str(lecturer.id) + ";"

        counter += 1

    lecturerDiff = lecturerContingent - counter

    for i in range(0, lecturerDiff):
        lecturersString = lecturersString + "" + ";"

    resourcesString = ";"
    for learningUnit in lecture.learningUnits:
        for resource in learningUnit.resources:
            resourcesString = resourcesString + resource.link + ";"

    lecture.description = lecture.description.replace(";", "")
    lecture.description = lecture.description.replace("\n", "")

    lectureArea = ""

    if len(lecture.areas) != 0:
        lectureArea = lecture.areas[0].name

    with open('problematicCollections.csv', 'a', encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(
            [lecture.name, lecture.description, lecturersString, lectureArea, lecture.semesterValue, resourcesString])


def uploadLectureFromOLW():
    collectionIds = requests.get(f'{urls["api"]}{urls["collectionIds"]}')
    collectionJson = collectionIds.json()
    uploaderTools = UploadFromOLW(client_id, client_secret, folder_id)
    counter = 0
    for collection in collectionJson:
        if counter <= alreadyUploaded:
            counter += 1
            continue

        singleCollection = get_collection(collection['id'])
        print("Upload der Collection: ")
        # print(json.dumps(singleCollection, indent=6, sort_keys=True))
        print(singleCollection)
        lectureName = singleCollection["name"]
        lectureDescription = singleCollection["description"]
        lectureLearningUnits = get_lectureUnits(singleCollection)
        lectureLecturers = get_lecturers(singleCollection)
        lectureAreas = get_areas(singleCollection)
        if "semesters" in singleCollection and len(singleCollection["semesters"]) != 0 and "areas" in singleCollection and len(singleCollection["areas"]) != 0:
            lectureSemesterValue = singleCollection["semesters"][0]["value"]
            print("Semester: " + str(lectureSemesterValue))
            print("Fachbereich: " + lectureAreas[0].name)
            tmpLecture = Lecture(lectureName, lectureDescription, lectureLearningUnits, lectureLecturers, lectureAreas,
                                 lectureSemesterValue)
            value = uploaderTools.transferCollectionAsPlaylist(tmpLecture)

            if not value:
                print("Problematische Collection erkannt...")
                print("Fuege diese zur Datenstruktur hinzu...")
                problematicCollections.append(singleCollection)
                tmpLecture = Lecture(lectureName, lectureDescription, lectureLearningUnits, lectureLecturers,
                                     lectureAreas,
                                     lectureSemesterValue)
                writeProblematicCollectionIntoCSV(tmpLecture)
                continue
        
            else:
                print("Collection erfolgreich hochgeladen!")

          #  counter += 1
        else:
            print("Problematische Collection erkannt...")
            print("Fuege diese zur Datenstruktur hinzu...")
            problematicCollections.append(singleCollection)
            tmpLecture = Lecture(lectureName, lectureDescription, lectureLearningUnits, lectureLecturers,
                                 lectureAreas,
                                 "NoSemesterGiven")
            writeProblematicCollectionIntoCSV(tmpLecture)


       # if counter == 10:
       #     break
