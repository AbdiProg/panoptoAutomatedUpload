import csv
from datetime import time
import time
import requests

from Tools.FileChooser import FileChooser
from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from panoptoDestinationFolderFinder import PanoptoFolderFinder
from uploadFromLink import UploadFromLink

#folder_id = 'ddce8d57-fcaa-402a-a1d1-afa900ec97d4'

problem_learning_units = []

lecturerContingent = 10

class UploadFromOLW:

    def __init__(self, client_id, client_secret, folder_id):

        self.oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, True)
        self.uploader = UploadFromLink(self.oauth2)
        self.requests_session = requests.Session()
        self.access_token = self.oauth2.get_access_token_authorization_code_grant()
        self.requests_session.headers.update({'Authorization': 'Bearer ' + self.access_token})
        self.folder_id = folder_id

    """<iframe src="______VIEWERURL_____&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>"""

    def writeIntoCSV(self, lecture, panoptoPlaylistLink):

        lecturersString = ";"
        counter = 0
        for lecturer in lecture.lecturers:
            """lecturersString = lecturersString + str(lecturer.id) + " " +lecturer.title + " " + lecturer.fullName + ","""

            if counter == len(lecture.lecturers) - 1:
                lecturersString = lecturersString + str(lecturer.id) + ";"
            else:
                lecturersString = lecturersString + str(lecturer.id) + ";"

            counter += 1

        lecturerDiff = lecturerContingent - counter

        for i in range(0, lecturerDiff):
            lecturersString = lecturersString + "" + ";"

        iFrameStr = "<iframe src='" + panoptoPlaylistLink + "&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all' " + "height='405' " + "width='720' " + "style='border: 1px solid #464646;' " + "allowfullscreen allow='autoplay'></iframe>"

        with open('collections.csv', 'a', encoding='utf-8') as file:
            write = csv.writer(file)
            write.writerow(
                [lecture.name, lecture.description, lecturersString, lecture.areas[0].name, lecture.semesterValue,
                 iFrameStr])

    def uploadSingleLearningUnit(self, learning_unit, folderID):
        name = learning_unit.name
        resources = learning_unit.resources

        # Name aufbauen
        for lecturer in learning_unit.lecturers:
            name = name + " " + lecturer.title + " " + lecturer.fullName

        pdfResourceLinks = []
        videoResourceLink = ""
        # Vorbereitung für die PanoptoBeschreibung
        resourceDescription = "{videoDescription} " \
                              "{attachmentDescription} " \
                              "{videoLicense} " \
                              "{attachmentLicense} "

        for resource in resources:
            fileChooser = FileChooser(resource.link, "https://olw-material.hrz.tu-darmstadt.de")
            optimalLinkVideoLink = fileChooser.getOptimalVideoLink()

            if optimalLinkVideoLink is not None and videoResourceLink == "":
                videoResourceLink = resource.link
                if resource.description != "":
                    resourceDescription = resourceDescription.replace("{videoDescription}", "Videobeschreibung: " + resource.description)
                else:
                    resourceDescription = resourceDescription.replace("{videoDescription}", " ")

                if resource.license != "":
                    resourceDescription = resourceDescription.replace("{videoLicense}", "Videolizenz: " + resource.license)
                else:
                    resourceDescription = resourceDescription.replace("{videoLicense}", " ")

            elif optimalLinkVideoLink is None:  # Falls es keinen optimalen VideoLink gibt, aber es sich trotzdem um eine
                # Ressource handelt, muss es eine PDF sein.

                pdfResourceLinks.append(resource.link)
                if resource.description != "":
                    resourceDescription = resourceDescription.replace("{attachmentDescription}", "Anhangbeschreibung: " +resource.description)
                else:
                    resourceDescription = resourceDescription.replace("{attachmentDescription}", " ")
                if resource.license != "":
                    resourceDescription = resourceDescription.replace("{attachmentLicense}", "Anhanglizenz: " +resource.license)
                else:
                    resourceDescription = resourceDescription.replace("{attachmentLicense}", " ")

        #    print(pdfResourceLinks[0])
        #   print(videoResourceLink)

        if len(pdfResourceLinks) == 1 and videoResourceLink is not None:
            return self.uploader.uploadVideoAndPdf(videoResourceLink, pdfResourceLinks[0],
                                                   "https://olw-material.hrz.tu-darmstadt.de",
                                                   folderID, name, resourceDescription)

        elif videoResourceLink is not None:
            resourceDescription = resourceDescription.replace("{attachmentDescription}", " ")
            resourceDescription = resourceDescription.replace("{attachmentLicense}", " ")

            return self.uploader.uploadSingleVideo(videoResourceLink, "https://olw-material.hrz.tu-darmstadt.de",
                                                   folderID, name, resourceDescription)

        else:
            problem_learning_units.append(learning_unit)

    # Eine ganze Collection / Lecture wird hier als Playlist auf Panopto übertragen.
    def transferCollectionAsPlaylist(self, lecture):
        name = lecture.name
        description = lecture.description.replace("\n", "")

        # Name aufbauen

        for lecturer in lecture.lecturers:
            name = name + " " + lecturer.title + " " + lecturer.fullName


        sessionIDs = []
        folderFinder = PanoptoFolderFinder(self.folder_id, self.requests_session)
        folderID = folderFinder.findDestinationFolderByString(lecture.areas[0].name, lecture.semesterValue)

        #Extra-Ordner für die Lecture
        payloadFolder = {'Name': name, 'Description': description, 'Parent': folderID}
        response = self.requests_session.post('https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/folders',
                                              json=payloadFolder)
        print("Waiting for Folder-Link...")
        time.sleep(3)
        responseJson = response.json()
        destinationFolderID = responseJson['Id']

        for learningUnit in lecture.learningUnits:
            sessionIDs.append(self.uploadSingleLearningUnit(learningUnit, destinationFolderID))

        payloadPlaylist = {'Name': name, 'Description': description,
                   'FolderId': destinationFolderID,
                   'Sessions': sessionIDs
                   }

        print(sessionIDs)
        response2 = self.requests_session.post('https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/playlists',
                                              json=payloadPlaylist)

        print("Waiting for Playlist-Link...")
        time.sleep(3)
        playlistResponseJson = response2.json()
        embedURL = playlistResponseJson['Urls']['EmbedUrl']
        print("Writing into CSV...")
        self.writeIntoCSV(lecture, embedURL)
        print("Finished!")
