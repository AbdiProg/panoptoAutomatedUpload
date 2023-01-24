#!python3
import argparse
from UploadAndAuthentification_Algo.panopto_oauth2 import PanoptoOAuth2
from UploadAndAuthentification_Algo.panopto_uploaderConstruct import PanoptoUploader


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

    folder_id = 'a901d04f-1915-477c-ace3-af5700a74577'

    client_id = '5aff5849-cfaa-4176-8a79-af82009b4df3'

    client_secret = 'R9d8ao5bM+BjWWpzcANElnVUZz3jP1ixH4OUHOpn5c0='

    upload_file = '../testvideo.mp4'

    videoTitle = input("Geben Sie den Videotitel an: ")
    videoDescription = input("Geben Sie die Videobeschreibung an: ")

    oauth2 = PanoptoOAuth2('test-tu-darmstadt.cloud.panopto.eu', client_id, client_secret, not args.skip_verify)

    uploader = PanoptoUploader('test-tu-darmstadt.cloud.panopto.eu', not args.skip_verify, oauth2, videoTitle,
                               videoDescription)

    uploader.upload_video(upload_file, folder_id)


if __name__ == '__main__':
    main()
