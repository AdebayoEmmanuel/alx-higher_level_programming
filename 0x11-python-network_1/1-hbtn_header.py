#!/usr/bin/python3
'''
This script fetches the value of X-Request-Id
for a request sent to url passed as param
'''


if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        output = dict(response.getheaders())
        print(output.get('X-Request-Id'))
