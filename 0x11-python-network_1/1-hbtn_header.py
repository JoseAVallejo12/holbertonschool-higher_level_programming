#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status."""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io') as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
