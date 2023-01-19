#!/usr/bin/python3


import urllib.request

'''This script fetches alx status endpoint'''


def hbtn_stat():
    '''fetches an endpoint and print some info about it'''
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        output = response.read()

    print("Body response:")
    print("\t - type:", type(output))
    print("\t - content:", output)
    print("\t - utf8 content:", output.decode("utf-8"))


if __name__ == "__main__":
    hbtn_stat()
