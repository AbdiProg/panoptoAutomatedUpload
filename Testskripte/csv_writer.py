

import csv
import xml.etree.ElementTree as ET
import pandas as pd
import xmltodict
import pprint
import json
import os

#HINWEIS: die erste Zeile der Keys muss noch gelöscht werden!

with open('Book1.csv') as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)

#TO DOS: iFrame String hinzufügen,


def add_column_to_csv():



    df = pd.read_csv('Book1.csv', sep=';')
    viewer_url = ['www.google.de']
    writer = df[df['Column4'] == 'test']
    tmp = writer
    tmp['viewer_url'] = viewer_url
    tmp.to_csv('newfile.csv', index=False)


add_column_to_csv()