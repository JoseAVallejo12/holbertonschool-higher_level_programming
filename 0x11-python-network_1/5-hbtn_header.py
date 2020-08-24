#!/usr/bin/python3
"""Script that fetches to url and get X-Request-Id."""
import requests
import sys

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    value = response.headers.get('X-Request-Id')
    print(value)
