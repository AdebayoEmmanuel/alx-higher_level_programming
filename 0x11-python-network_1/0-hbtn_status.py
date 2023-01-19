#!/usr/bin/python3
'''This script fetches alx status endpoint'''


if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        output = response.read()

        print("Body response:")
        print("\t - type:", type(output))
        print("\t - content:", output)
        print("\t - utf8 content:", output.decode("utf-8"))
