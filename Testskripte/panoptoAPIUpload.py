# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:48:32 2023

@author: Abdulhaq
"""

from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from UploadAndAuthentificationPanopto_Algo.panopto_uploaderConstruct import PanoptoUploader
import requests
import os

older_id = 'a901d04f-1915-477c-ace3-af5700a74577'
    
client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

client_secret = 'S3Ndzc9QEU52PUuTxbctEz6H014LnLkIuaqmW/5xFWU='

upload_file = 'testvideo.mp4'


oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, True)

#uploader = PanoptoUploader('test-tu-darmstadt.cloud.panopto.eu', True, oauth2, videoTitle, videoDescription)


requests_session = requests.Session()
access_token = oauth2.get_access_token_authorization_code_grant()
requests_session.headers.update({'Authorization': 'Bearer ' + access_token})

directory = input("Geben Sie bitte den Quellordnerpfad mit allen Ordnern an: ")
parentPanoptoID = input("Geben Sie bitte die ZielordnerID aus Panopto an: ")

def mergeIntoPlaylist(sessionArray, playlistName, folderID):
    payload = {'Name': playlistName, 'Description': '', 'FolderId': folderID, 
               'Sessions': sessionArray
            }
    response = requests_session.post('https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/playlists', json=payload)

#Die directoryPanoptoID ist konkret eine OrdnerID für einen Fachbereich
def uploadVideos(sourcePath, directoryPanoptoID):
    
    for playlistname in os.listdir(sourcePath): #Hier iteriert man durch die zukünftigen Playlists, die noch als Ordner vorhanden sind.  
   
        p = os.path.join(sourcePath, playlistname) 
        
        payload = {'Name': playlistname, 'Parent': directoryPanoptoID}
        resp = requests_session.post("https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/folders", payload)
        responseJson = resp.json()
        playlistDirectoryID = responseJson['Id']
        
        if os.path.isdir(p):
            for videoname in os.listdir(p):
               v = os.path.join(p, videoname) 
               uploader = PanoptoUploader('test-tu-darmstadt.cloud.panopto.eu', True, oauth2, videoname, "Ein TestVideo")
               uploader.upload_video(v, playlistDirectoryID)
            respVideos = requests_session.get("https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/folders/{0}/sessions".format(playlistDirectoryID))
            respVideosJson = respVideos.json()
            sessionArray = []
            for i in range(0, len(respVideosJson['Results'])):
                #print(respVideosJson['Results'][i]['Id'])
                sessionArray.append(respVideosJson['Results'][i]['Id'])
            mergeIntoPlaylist(sessionArray, playlistname, playlistDirectoryID)
            
def createFoldersWithAPI(directory, parentPanoptoID):
    for filename in os.listdir(directory):
     f = os.path.join(directory, filename)
     # checking if it is a file
     if os.path.isdir(f):
         payload = {'Name': filename, 'Parent': parentPanoptoID}
         resp = requests_session.post("https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/folders", payload)
         responseJson = resp.json()
         uploadVideos(f, responseJson['Id'])
         print(responseJson['Id'])


#directoryPanoptoID = "b73dd194-dea3-47ff-ba34-af8d00c7e113"
#respVideos = requests_session.get("https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/folders/{0}/sessions".format(directoryPanoptoID))
#respVideosJson = respVideos.json()
#print(respVideosJson['Results'][0]['Id'])
#arr = ['148ff6b9-ee12-4880-86ba-af8d00cf13a9', 'f724926d-88fa-4002-a79d-af8d00cebb88']
#payload = {'Name': 'AutomatedPlaylist', 'Description': 'Automatisch erstellte Playlist', 'FolderId': 'b04899dd-a47a-461c-b9a4-af8d00cea5c5', 
#             'Sessions': arr
#           }
#response = requests_session.post('https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/playlists', json=payload)
#response2 = requests_session.delete('https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/playlists/36fe73c2-4718-45c9-9c08-af8d00cf4377')


createFoldersWithAPI(directory, parentPanoptoID)
         