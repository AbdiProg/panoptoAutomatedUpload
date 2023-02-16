from textwrap import wrap

import requests
import json
import pandas as pd
from dicttoxml import dicttoxml
import xml.etree.ElementTree as Xet
import csv

#####Folder-Name-Extraction#####
#####This Script provides a method named returnArrayForFolderNameIdentification, which returns a array with all "areas" and "semesters".
#####Those "areas" and "semesters" will be used to create panopto folders with specific names#####

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


resources = [r for r in get_resources() if not r['deleted'] and r['name']]


# print(json.dumps(resources, indent=10, sort_keys=True))

def returnArrayForFolderNameIdentification():
    areas = []
    semesters = []

    for r in resources:
        uuidPath = '/'.join(wrap(r['uuid'].replace('-', ''), 2))
        if f'{r["areas"]}' != "[]":
            if not areas.__contains__(f'{r["areas"][0]["name"]}'):
                areas.append(f'{r["areas"][0]["name"]}')

        if f'{r["semesters"]}' != "[]":
            if not semesters.__contains__(f'{r["semesters"][0]["value"]}'):
                semesters.append(f'{r["semesters"][0]["value"]}')

    identifiers = [areas, semesters]
    # print(identifiers)
    return identifiers


#returnArrayForFolderNameIdentification()
