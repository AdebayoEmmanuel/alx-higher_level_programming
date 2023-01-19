#!/usr/bin/python3
import urllib.request

'''This script fetches alx status endpoint'''
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    output = response.read()

print("Body response:")
print("\t - type:", type(output))
print("\t - content:", output)
print("\t - utf8 content:", output.decode("utf-8"))
