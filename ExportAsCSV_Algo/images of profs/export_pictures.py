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

def get_pic_of_prof(id):

    response = requests.get(f'{urls["profs"]}{id}')
    json_file = json.loads(response.text)
    print(json_file['photoAvailable'])
    if json_file['photoAvailable'] == True:

        #script for downloading a picture
        url = 'https://openlearnware.de/olw-rest-db/api/user/'+str(id)+'/photo'  # prompt user for img url
        file_name = str(id)+'.png'  # prompt user for file_name

        res = requests.get(url, stream=True)

        if res.status_code == 200:
            with open(file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ', file_name)
        else:
            print('Image Couldn\'t be retrieved')



response = requests.get(f'{urls["profs"]}')
json_file = json.loads(response.text)
print(json_file)


for i in range(365):
 get_pic_of_prof(i+1)
