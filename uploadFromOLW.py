from Tools.FileChooser import FileChooser
from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from uploadFromLink import UploadFromLink

folder_id = 'ddce8d57-fcaa-402a-a1d1-afa900ec97d4'

client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

client_secret = 'WB1eyMbrDnP23QxOkhRR/8GXNJGhwxQhV+6aOMFooBw='

problem_learning_units = []


def uploadSingleLearningUnit(learning_unit):
    name = learning_unit.name
    resources = learning_unit.resources

    # Name aufbauen
    for lecturer in learning_unit.lecturers:
        name = name + "-" + lecturer.title + " " + lecturer.fullName

    pdfResourceLinks = []
    videoResourceLink = ""
    # Vorbereitung für die PanoptoBeschreibung
    resourceDescription = "Videobeschreibung: {videoDescription}" \
                          "Anhangbeschreibung: {attachmentDescription}" \
                          "Videolizenz: {videoLicense}" \
                          "Anhanglizenz: {attachmentLicense}"

    for resource in resources:
        fileChooser = FileChooser(resource.link, "https://olw-material.hrz.tu-darmstadt.de")
        optimalLinkVideoLink = fileChooser.getOptimalVideoLink()

        if optimalLinkVideoLink is not None and videoResourceLink == "":
            videoResourceLink = resource.link
            if resource.description != "":
                resourceDescription = resourceDescription.replace("{videoDescription}", resource.description)
            else:
                resourceDescription = resourceDescription.replace("{videoDescription}", "")

            if resource.license != "":
                resourceDescription = resourceDescription.replace("{videoLicense}", resource.license)
            else:
                resourceDescription = resourceDescription.replace("{videoLicense}", "")

        elif optimalLinkVideoLink is None:  # Falls es keinen optimalen VideoLink gibt, aber es sich trotzdem um eine
            # Ressource handelt, muss es eine PDF sein.

            pdfResourceLinks.append(resource.link)
            if resource.description != "":
                resourceDescription = resourceDescription.replace("{attachmentDescription}", resource.description)
            else:
                resourceDescription = resourceDescription.replace("{attachmentDescription}", "")
            if resource.license != "":
                resourceDescription = resourceDescription.replace("{attachmentLicense}", resource.license)
            else:
                resourceDescription = resourceDescription.replace("{attachmentLicense}", "")

    oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, True)
    uploader = UploadFromLink(oauth2)

    if pdfResourceLinks == 1 and videoResourceLink is not None:
        uploader.uploadVideoAndPdf(videoResourceLink, pdfResourceLinks[0], "https://olw-material.hrz.tu-darmstadt.de",
                                   folder_id, name, resourceDescription)

    else:
        problem_learning_units.append(learning_unit)