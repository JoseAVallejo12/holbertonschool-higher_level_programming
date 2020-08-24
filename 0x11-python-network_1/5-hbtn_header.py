#!/usr/bin/python3
"""Script that fetches to url and get X-Request-Id."""
import requests

if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    print(r.headers['X-Request-Id'])
