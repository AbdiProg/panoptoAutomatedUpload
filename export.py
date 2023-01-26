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
    'convFiles': 'https://olw-material.hrz.tu-darmstadt.de/olw-kov-repository/material/',
}


def get_collection(collection_id):
    response = requests.get(f'{urls["api"]}{urls["collection"]}{collection_id}')
    return json.loads(response.text)


def get_resources():
    response = requests.get(f'{urls["api"]}{urls["resources"]}')
    json_file = json.loads(response.text)
    xml = dicttoxml(json_file)
    print(xml)
    return json_file


resources = [r for r in get_resources() if not r['deleted'] and r['name']]

print(json.dumps(resources, indent = 10, sort_keys=True))

for r in resources:
    uuidPath = '/'.join(wrap(r['uuid'].replace('-', ''), 2))
    resource = {'name': f'{r["name"]}',
                'description': f'{r["description"]}',
                'author': f'{r["users"][0]["firstName"]}',
                'collection': f'{r["collections"]}',
                'rawFileDir': f'{urls["rawFiles"]}{uuidPath}',
                'convFileDir': f'{urls["convFiles"]}{uuidPath}',

                }

    with open('mycsvfile.csv', 'a') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.DictWriter(f, resource.keys())
        if f.tell() == 0:
            w.writeheader()
        w.writerow(resource)

with open('mycsvfile.csv', newline='') as in_file:
    with open('olw_ressources.csv', 'w', newline='') as out_file:
         writer = csv.writer(out_file)
         for row in csv.reader(in_file):
            if any(row):
                 writer.writerow(row)

    #print(resource)

#print(len(resources))
