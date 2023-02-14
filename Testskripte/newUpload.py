#!python3
import argparse
from UploadAndAuthentificationPanopto_Algo.panopto_oauth2 import PanoptoOAuth2
from UploadAndAuthentificationPanopto_Algo.panopto_uploaderConstruct import PanoptoUploader
import pathlib


def parse_argument():
    '''
    Argument definition and handling.
    '''
    parser = argparse.ArgumentParser(description='Upload a single video file to Panopto server')
    # parser.add_argument('--server', dest='server', required=True, help='Server name as FQDN')
    # parser.add_argument('--folder-id', dest='folder_id', required=True, help='ID of target Panopto folder')
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
    print("Hallo!")
    # if args.skip_verify:
    #     # This line is needed to suppress annoying warning message.
    #     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    folder_id = 'a2d83c8e-fdea-490a-8fb1-af82009b28de'

    client_id = '368929b5-aabf-4e43-9bc0-af82009ab95c'

    client_secret = 'InDuReCsQw0EujzyGRYDfngM5t7JbIT80l9vQdi6AXw='

    upload_file = pathlib.Path(r'C:\Users\domin\panoptoAutomatedUpload\testvideo.mp4').as_uri()
    #upload_file = 'https://olw-material.hrz.tu-darmstadt.de/olw-konv-repository/material/01/13/88/10/e5/92/11/e3/b7/15/00/50/56/bd/73/ad/2.mp4'
    videoTitle = input("Geben Sie den Videotitel an: ")
    videoDescription = input("Geben Sie die Videobeschreibung an: ")

    oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, not args.skip_verify)

    uploader = PanoptoUploader('test-tu-darmstadt.cloud.panopto.eu', not args.skip_verify, oauth2, videoTitle,
                               videoDescription)

    uploader.upload_video(upload_file,"", folder_id)




if __name__ == '__main__':
    main()
