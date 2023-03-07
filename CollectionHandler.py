import ctypes
from textwrap import wrap

import requests
import json
import pandas as pd
from dicttoxml import dicttoxml
import xml.etree.ElementTree as Xet
import csv

from Objects.LearningUnit import LearningUnit
from Objects.Resource import Resource
from Objects.Area import Area
from Objects.Lecture import Lecture
from Objects.Lecturer import Lecturer

urls = {
    'api': 'https://openlearnware.tu-darmstadt.de/olw-rest-db/api',
    'collectionIds': '/collection-overview/filter/index/all?pick=id&pick=name',
    'collection': '/collection-detailview/index/',
    'resources': '/resource-overview/filter/index/all?deleted=false',
    'rawFiles': 'https://olw-material.hrz.tu-darmstadt.de/olw-roh-repository/archive/',
    'convFiles': 'https://olw-material.hrz.tu-darmstadt.de/olw-konv-repository/material/',
    'users': '/user/',
}


def get_collection(collection_id):
    response = requests.get(f'{urls["api"]}{urls["collection"]}{collection_id}')
    return json.loads(response.text)


def get_resources():
    response = requests.get(f'{urls["api"]}{urls["resources"]}')
    json_file = json.loads(response.text)
    xml = dicttoxml(json_file)
    # print(xml)
    return json_file


# resources = [r for r in get_resources() if not r['deleted'] and r['name']]

"""
def get_resources_outOfCollectionID(collection_id):
    for r in resources:
        if f'{r["collections"]}' != "[]":
            if f'{r["collections"][0]["id"]}' == str(collection_id):
                uuidPath = '/'.join(wrap(r['uuid'].replace('-', ''), 2))
                resource = {'name': f'{r["name"]}',
                            'description': f'{r["description"]}',
                            'areas': f'{r["name"]}',
                            'author': f'{r["users"]}',
                            'collection': f'{r["collections"]}',
                            'code': f'{r["code"]}',
                            'rawFileDir': f'{urls["rawFiles"]}{uuidPath}',
                            'convFileDir': f'{urls["convFiles"]}{uuidPath}',
                            'viewerUrl': None,
                            'iFrame': None
                            }
                print(json.dumps(resource, indent=6, sort_keys=True))

"""


def checkIfCollectionElementIsInRubric(collectionElement, rubric):
    if collectionElement in rubric:
        return True
    return False


def get_areas(jsonData):
    areas = jsonData["areas"]
    areaObjects = []
    for area in areas:
        tmpArea = Area(area['id'], area['name'])
        areaObjects.append(tmpArea)

    return areaObjects


def get_lecturers(jsonData):
    users = jsonData["users"]
    userObjects = []
    for user in users:
        urlLink = f'{urls["api"]}{urls["users"]}{user["id"]}'
        response = requests.get(urlLink)
        responseJson = response.json()
        photoLink = ""
        if responseJson['photoAvailable']:
            photoLink = f'{urls["api"]}{urls["users"]}{user["id"]}{"/photo"}'
        tmpUser = Lecturer(responseJson['id'], responseJson['title'], responseJson['firstName'],
                           responseJson['lastName'],
                           responseJson['email'], responseJson['organization'], responseJson['website'],
                           responseJson['about'], responseJson['name'], photoLink)
        userObjects.append(tmpUser)

    return userObjects


jsonOfAllResources = get_resources()
def get_resourceDescription(uuid):
    array2 = jsonOfAllResources
    filtered_list = [
        resource for resource in array2
        if resource['uuid'] == uuid
    ]
    return filtered_list[0]['description']


def get_singleResource2(jsonData, element):
    uuidPath = '/'.join(wrap(jsonData["resources"][str(element)]['uuid'].replace('-', ''), 2))
    link = f'{urls["convFiles"]}{uuidPath}'

    resourceJson = jsonData["resources"][str(element)]
    resourceLicense = resourceJson["license"]["code"]
    resourceType = resourceJson["type"]
    #resourceDescription =
    return Resource(resourceType, link, resourceLicense, get_resourceDescription(jsonData["resources"][str(element)]['uuid']))


def get_lectureUnits(jsonData):
    collectionElements = jsonData["collectionElements"]
    lectureUnitObjects = []

    for element in collectionElements:
        if str(element) in jsonData["rubrics"]:
            rubricJson = jsonData["rubrics"][str(element)]
            learningUnitName = jsonData["rubrics"][str(element)]["name"]
            lectureUnitLecturers = get_lecturers(
                jsonData["resources"][str(jsonData["rubrics"][str(element)]["resources"][0])])
            resources = []
            for resource in rubricJson["resources"]:
                resources.append(get_singleResource2(jsonData, str(resource)))

            tmpLearningUnitObject = LearningUnit(learningUnitName, resources, lectureUnitLecturers)
            lectureUnitObjects.append(tmpLearningUnitObject)
        else:
            learningUnitName = jsonData["resources"][str(element)]["name"]
            lectureUnitLecturers = get_lecturers(jsonData["resources"][str(element)])
            resources = [get_singleResource2(jsonData, str(element))]
            tmpLearningUnitObject = LearningUnit(learningUnitName, resources, lectureUnitLecturers)
            lectureUnitObjects.append(tmpLearningUnitObject)

    return lectureUnitObjects


def get_informationOfCollection(collection_id):
    singleCollection = get_collection(collection_id)
    lectureName = singleCollection["name"]
    lectureDescription = singleCollection["description"]
    lectureLearningUnits = get_lectureUnits(singleCollection)
    lectureLecturers = get_lecturers(singleCollection)
    lectureAreas = get_areas(singleCollection)
    lectureSemesterValue = singleCollection["semesters"][0]["value"]

    tmpLecture = Lecture(lectureName, lectureDescription, lectureLearningUnits, lectureLecturers, lectureAreas,
                         lectureSemesterValue)
    return tmpLecture


def get_informationOfAllCollections():
    collectionIds = requests.get(f'{urls["api"]}{urls["collectionIds"]}')
    collectionJson = collectionIds.json()
    lectures = []
    for collection in collectionJson:
        singleCollection = get_collection(collection['id'])
        lectureName = singleCollection["name"]
        lectureDescription = singleCollection["description"]
        lectureLearningUnits = get_lectureUnits(singleCollection)
        lectureLecturers = get_lecturers(singleCollection)
        lectureAreas = get_areas(singleCollection)
        lectureSemesterValue = singleCollection["semester"]["value"]

        tmpLecture = Lecture(lectureName, lectureDescription, lectureLearningUnits, lectureLecturers, lectureAreas,
                             lectureSemesterValue)
        lectures.append(tmpLecture)

    return lectures


# print(get_collection(78))
# print(json.dumps(get_collection(42), indent=6, sort_keys=True))


# print(get_collection(78))
# get_informationOfAllCollections()
# get_resources_outOfCollectionID(78)

"""
# Collection-Test
responseJson = get_collection(350)
# print(responseJson["collectionElements"])  #
print(get_lectureUnits(responseJson))
# print(responseJson["rubrics"]["867"]["name"])
# print(responseJson["rubrics"]['1970'])
print(json.dumps(responseJson, indent=6, sort_keys=True))
# print(responseJson ["resources"][str(responseJson["rubrics"]["867"]["resources"][0])])
# print(get_lecturers(responseJson))
for lec in get_lectureUnits(responseJson):
    print(lec.name)
    for res in lec.resources:
        print(res)
# responseJson2 = get_collection(42)
# print(json.dumps(get_collection(42), indent=6, sort_keys=True))
# print(checkIfCollectionElementIsInRubric('191', responseJson["rubrics"])) #Geht!
"""

responseJson = get_collection(373)
print(json.dumps(responseJson, indent=6, sort_keys=True))
print(get_informationOfCollection("373").learningUnits[2].resources[0])