from textwrap import wrap

import requests
import json
import pandas as pd
from dicttoxml import dicttoxml
import xml.etree.ElementTree as Xet
import csv

urls = {
    'api': 'https://openlearnware.tu-darmstadt.de/olw-rest-db/api',
    'collectionIds': '/collection-overview/filter/index/all?pick=id&pick=name',
    'collection': '/collection-detailview/index/',
    'resources': '/resource-overview/filter/index/all?deleted=false',
    'rawFiles': 'https://olw-material.hrz.tu-darmstadt.de/olw-roh-repository/archive/',
    'convFiles': 'https://olw-material.hrz.tu-darmstadt.de/olw-konv-repository/material/',
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


#resources = [r for r in get_resources() if not r['deleted'] and r['name']]

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

def get_informationOfAllCollections():
    collectionIds = requests.get(f'{urls["api"]}{urls["collectionIds"]}')
    collectionJson = collectionIds.json()
    lectures = []
    for collection in collectionJson:
        singleCollection = get_collection(collection['id'])
        # print(singleCollection["resources"])

# print(get_collection(78))
#print(json.dumps(get_collection(42), indent=6, sort_keys=True))


# print(get_collection(78))
# get_informationOfAllCollections()
#get_resources_outOfCollectionID(78)


#Collection-Test
responseJson = get_collection(78)
print(responseJson["collectionElements"])
print(responseJson["rubrics"]['1970'])
responseJson2 = get_collection(42)
print(json.dumps(get_collection(42), indent=6, sort_keys=True))
print(checkIfCollectionElementIsInRubric('191', responseJson["rubrics"])) #Geht!