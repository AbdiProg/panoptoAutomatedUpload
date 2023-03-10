from textwrap import wrap

import requests
import json
import pandas as pd
from dicttoxml import dicttoxml
import xml.etree.ElementTree as Xet
import csv

import requests # request img from web
import shutil # save img locally

urls = {
    'api': 'https://openlearnware.tu-darmstadt.de/olw-rest-db/api',
    'collectionIds': '/collection-overview/filter/index/all?pick=id&pick=name',
    'collection': '/collection-detailview/index/',
    'resources': '/resource-overview/filter/index/all?deleted=false',
    'rawFiles': 'https://olw-material.hrz.tu-darmstadt.de/olw-roh-repository/archive/',
    'convFiles': 'https://olw-material.hrz.tu-darmstadt.de/olw-konv-repository/material/',
    'profs': 'https://openlearnware.de/olw-rest-db/api/user/'
}
#https://openlearnware.de/olw-rest-db/api/user/ für die Information zu den Professoren

def get_collection(collection_id):
    response = requests.get(f'{urls["api"]}{urls["collection"]}{collection_id}')
    return json.loads(response.text)


def get_resources():
    response = requests.get(f'{urls["api"]}{urls["resources"]}')
    json_file = json.loads(response.text)
    xml = dicttoxml(json_file)
    #print(xml)
    return json_file


resources = [r for r in get_resources() if not r['deleted'] and r['name']]

#print(json.dumps(resources, indent=10, sort_keys=True))

# for r in resources:
#     uuidPath = '/'.join(wrap(r['uuid'].replace('-', ''), 2))
#     resource = {'name': f'{r["name"]}',
#                 'description': f'{r["description"]}',
#                 'areas': f'{r["name"]}',
#                 'author': f'{r["users"]}',
#                 'collection': f'{r["collections"]}',
#                 'code': f'{r["code"]}',
#                 'rawFileDir': f'{urls["rawFiles"]}{uuidPath}',
#                 'convFileDir': f'{urls["convFiles"]}{uuidPath}',
#                 'viewerUrl': None,
#                 'iFrame': None
#                 }
    #vielleicht packen wir den Uploader direkt hier rein?
    #Der Upload link wird ja sowieso über die convFileDir erstellt. Dann können wir hier direkt die Daten für den iFrame abrufen
    #
    #
    # #writes all metadata in csv table
    # with open('mycsvfile.csv', 'a') as f:  # You will need 'wb' mode in Python 2.x
    #     w = csv.DictWriter(f, resource.keys())
    #     if f.tell() == 0:
    #         w.writeheader()
    #     w.writerow(resource)

#
# #removes the empty rows of the csv table
# with open('mycsvfile.csv', newline='') as in_file:
#     with open('olw_ressources.csv', 'w', newline='') as out_file:
#         writer = csv.writer(out_file)
#         for row in csv.reader(in_file):
#             if any(row):
#                 writer.writerow(row)


#methode für das Überschreiben der csv nach dem Upload:

#test = get_collection(78)

#print(test)
#print(json.dumps(test, indent=10, sort_keys=True))



def get_prof(id):
    response = requests.get(f'{urls["profs"]}{id}')
    json_file = json.loads(response.text)
    if json_file['photoAvailable'] == True:
        json_file['photoAvailable'] = '<img src="'+'https://openlearnware.de/olw-rest-db/api/user/' +str(id)+'/photo'+'">'
    return json_file


for i in range(365):
    file = get_prof(i+1)
# #writes all metadata in csv table
    with open('../OtherCSVData/profs.csv', 'a') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.DictWriter(f, file.keys())
        if f.tell() == 0:
            w.writeheader()
        w.writerow(file)

    #removes the empty rows of the csv table
    with open('../OtherCSVData/profs.csv', newline='') as in_file:
        with open('../OtherCSVData/profs_formated.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if any(row):
                    writer.writerow(row)