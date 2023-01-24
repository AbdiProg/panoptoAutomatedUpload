#Uploadtest with PDF-Slides
from UploadAndAuthentification_Algo.panopto_oauth2 import PanoptoOAuth2
from UploadAndAuthentification_Algo.panopto_uploaderConstruct import PanoptoUploader


client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

client_secret = 'R9d8ao5bM+BjWWpzcANElnVUZz3jP1ixH4OUHOpn5c0='

upload_file = 'C:/Users/Abdulhaq/PycharmProjects/panoptoProjekt/testvideo.mp4'
upload_pdffile = 'C:/Users/Abdulhaq/PycharmProjects/panoptoProjekt/tuda_logo.pdf'
folder_id = '3dc10920-7577-4c19-991c-af8d00e5cdd9'


videoTitle = "TestVideoMitPDF"
videoDescription = "TestVideoMitPDF"

oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, True)

uploader = PanoptoUploader('test-tu-darmstadt.cloud.panopto.eu', True, oauth2, videoTitle, videoDescription)


uploader.upload_video(upload_file, upload_pdffile, folder_id)