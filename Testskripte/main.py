import csv
import urllib
from urllib.request import urlopen

from uploadFromLink import UploadFromLink

#uploader = UploadFromOLW("")

#uploader.uploadSingleVideo('https://olw-material.hrz.tu-darmstadt.de/olw-konv-repository/material/1d/6c/4d/a0/a7/53/11/e6/83/64/00/50/56/bd/73/ae', "3dc10920-7577-4c19-991c-af8d00e5cdd9")

"""
link = 'https://olw-material.hrz.tu-darmstadt.de/olw-konv-repository/material/1d/6c/4d/a0/a7/53/11/e6/83/64/00/50/56/bd/73/ae/3.mp4'

#f = urlopen(link)
#myfile = f.read(400)
req = urllib.request.Request(link,
                                          method='HEAD')
f = urllib.request.urlopen(req)

while True:
    data = f.read(4000000)
    print(data)
"""

#CSV Reader
with open('C:/Users/Abdulhaq/PycharmProjects/panoptoProjekt/ExportAsCSV_Algo/mycsvfile.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)