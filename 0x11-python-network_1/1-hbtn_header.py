#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status."""
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
