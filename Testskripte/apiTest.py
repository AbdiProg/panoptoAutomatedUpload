#!python3
import argparse
from UploadAndAuthentification_Algo.panopto_oauth2 import PanoptoOAuth2
import requests
import os

def parse_argument():
    '''
    Argument definition and handling.
    '''
    parser = argparse.ArgumentParser(description='Upload a single video file to Panopto server')
    #parser.add_argument('--server', dest='server', required=True, help='Server name as FQDN')
    #parser.add_argument('--folder-id', dest='folder_id', required=True, help='ID of target Panopto folder')
   # parser.add_argument('--upload-file', dest='upload_file', required=True, help='File to be uploaded')
   # parser.add_argument('--client-id', dest='client_id', required=True, help='Client ID of OAuth2 client')
   # parser.add_argument('--client-secret', dest='client_secret', required=True, help='Client Secret of OAuth2 client')
    parser.add_argument('--skip-verify', dest='skip_verify', action='store_true', required=False,
                        help='Skip SSL certificate verification. (Never apply to the production code)')

    return parser.parse_args()


def main():
  '''
  Main method
  '''
  args = parse_argument()
 
 #if args.skip_verify:
#     # This line is needed to suppress annoying warning message.
#     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

  client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'
 
  client_secret = 'R9d8ao5bM+BjWWpzcANElnVUZz3jP1ixH4OUHOpn5c0='

 
  oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, not args.skip_verify)
 
  requests_session = requests.Session()
  access_token = oauth2.get_access_token_authorization_code_grant()
   #Beispiel Anfragen
  # requests_session.headers.update({'Authorization': 'Bearer ' + access_token})
  # response = requests.get('http://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/auth/legacyLogin')
  # response = requests_session.get('https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/folders/e7a1b480-5ec7-438b-a484-af5f00a442cc/sessions')
  # payload = {'Name': 'AutomatedPlaylist', 'Description': 'Automatisch erstellte Playlist', 'FolderId': 'e7a1b480-5ec7-438b-a484-af5f00a442cc', 
  #            'Sessions': ['ae963742-025e-4396-9983-af5f00a44823']
  #            }
  # response = requests_session.post('https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/playlists', json=payload)
  response = requests_session.get("https://test-tu-darmstadt.cloud.panopto.eu/Panopto/api/v1/sessions/b8c3f739-71c6-410a-adc7-af8d00bcd41a")
  print(response.json())

   #############################################################

  #mainFolderPath = 'C:/Users/Abdulhaq/.spyder-py3/FachbereichsOrdner'  
  directory = 'C:/Users/Abdulhaq/.spyder-py3/FachbereichsOrdner'
  for filename in os.listdir(directory):
     f = os.path.join(directory, filename)
     # checking if it is a file
     #if os.path.isdir(f):
                  
       

  if __name__ == '__main__':
      main()
    
def createFolder (file_path):
      print("Test")
    