#!python3
"""Authorization sample, as Server-side Web Application."""
import sys
import argparse
import requests
import urllib3
import time
import pandas as pd
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..', 'common')))
from panopto_oauth2 import PanoptoOAuth2


def parse_argument():
    parser = argparse.ArgumentParser(description='Sample of Authorization as Server-side Web Application')
    parser.add_argument('--server', dest='server', required=True, help='Server name as FQDN')
    parser.add_argument('--client-id', dest='client_id', required=True, help='Client ID of OAuth2 client')
    parser.add_argument('--client-secret', dest='client_secret', required=True, help='Client Secret of OAuth2 client')
    parser.add_argument('--skip-verify', dest='skip_verify', action='store_true', required=False, help='Skip SSL certificate verification. (Never apply to the production code)')
    return parser.parse_args()


def main():
    """First function called from command line."""
    args = parse_argument()

    if args.skip_verify:
        # This line is needed to suppress annoying warning message.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Use requests module's Session object in this example.
    # ref. https://2.python-requests.org/en/master/user/advanced/#session-objects
    requests_session = requests.Session()
    requests_session.verify = not args.skip_verify

    # Load OAuth2 logic
    oauth2 = PanoptoOAuth2(args.server, args.client_id, args.client_secret, not args.skip_verify)

    # Initial authorization
    authorization(requests_session, oauth2)

    sessionID = '9325e8f9-c0d5-4a6e-8a49-afa90008c202'

    # call public API for viewer URL with session ID
    print('calling GET----------------------------------------------------------------------------------')
    url = 'https://{0}/Panopto/api/v1/sessions/{1}'.format(args.server, sessionID)
    response = requests_session.get(url)
    data = response.json()

    #eventuell generieren wir hier die upload csv über ein dictionary da wir auch erst hier die session id haben
    # und hier haben wir dann auch die Manifest Datei mit allen wichtigen Metadaten

    print(data)
    print(data['Urls']['ViewerUrl'])


def authorization(requests_session, oauth2):
    # Go through authorization
    access_token = oauth2.get_access_token_authorization_code_grant()
    # Set the token as the header of requests
    requests_session.headers.update({'Authorization': 'Bearer ' + access_token})

def inspect_response_is_unauthorized(response):
    '''
    Inspect the response of a requets' call, and return True if the response was Unauthorized.
    An exception is thrown at other error responses.
    Reference: https://stackoverflow.com/a/24519419
    '''
    if response.status_code // 100 == 2:
        # Success on 2xx response.
        return False

    if response.status_code == requests.codes.unauthorized:
        print('Unauthorized. Access token is invalid.')
        return True

    # Throw unhandled cases.
    response.raise_for_status()


if __name__ == '__main__':
    main()