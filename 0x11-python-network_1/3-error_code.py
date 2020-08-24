#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status."""
from urllib import request
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except Exception as a:
        print("Error code: {}".format(a.code))
