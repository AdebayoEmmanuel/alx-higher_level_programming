#!/usr/bin/python3
'''
This script sends request to a server
Prints the body of the respose
and error code in case of error
'''

import urllib.request
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as res:
        output = res.read()
        print(output.decode('utf-8'))
except urllib.error.HTTPError as err:
    print(f"Error code: {err.code}")
