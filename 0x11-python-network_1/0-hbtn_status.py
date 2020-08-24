#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    s = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}\n"
    print(s.format(type(html), html, html.decode("utf-8"), end=""))
