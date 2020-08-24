#!/usr/bin/python3
"""Script that fetches to url and get X-Request-Id."""
import requests
import sys

if __name__ == '__main__':
    params = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=params)
    print(response.text)
