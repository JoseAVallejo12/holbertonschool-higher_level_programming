#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/stat."""
import requests

if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    s = "Body response:\n\t- type: {}\n\t- content: {}"
    print(s.format(type(r.text), r.text))
