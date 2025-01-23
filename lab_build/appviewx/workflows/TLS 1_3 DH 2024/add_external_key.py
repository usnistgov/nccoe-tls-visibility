#!/usr/bin/env python

import requests, argparse, base64


def add_external_key(server_url, token, uuid, der_filename, ssl_verify=True):
    with open(der_filename, 'rb') as der_file:
        resp = requests.post(
            '%s/externalkeys/'%server_url,
            headers={'Authorization': 'Token %s'%token},
            data={
                'external_keys_uuid': uuid,
                'asymmetric_key_package': base64.b64encode(der_file.read()),
            },
            verify=ssl_verify,
        )
        resp.raise_for_status()
        print('Added.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server-url', dest='server_url', required=True,
                        help='url for the rest service.\ne.g. https://my-appliance/api for '
                             'external access or http://localhost:8000 for internal access.')
    parser.add_argument('-t', '--token', dest='token', required=True)
    parser.add_argument('-u', '--uuid', dest='uuid', required=True)
    parser.add_argument('-d', '--der-filename', dest='der_filename', required=True)
    parser.add_argument('-n', '--noverify', dest='noverify', default=False, action='store_true',
                        help='do not require a signed certificate')

    args = parser.parse_args()

    add_external_key(args.server_url, args.token, args.uuid, args.der_filename, not args.noverify)
