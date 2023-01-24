from textwrap import wrap

import requests
import json

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
    return json.loads(response.text)


resources = [r for r in get_resources() if not r['deleted'] and r['name']]

resourcesArray = []

for r in resources:
    uuidPath = '/'.join(wrap(r['uuid'].replace('-', ''), 2))
    resource = {'name': f'{r["name"]}',
                'description': f'{r["description"]}',
                'collection': f'{r["collections"]}',
                'area': f'{r["areas"]}',
                'code': f'{r["code"]}',
                'semester': f'{r["semesters"]}',
                'rawFileDir': f'{urls["rawFiles"]}{uuidPath}',
                'convFileDir': f'{urls["convFiles"]}{uuidPath}',
                }
    resourcesArray.append(resource.get("convFileDir"))
print(json.dumps(resources, indent = 4, sort_keys=True))
print(resourcesArray)
