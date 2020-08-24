#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()

print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}"""
      .format(type(html), html, html.decode("utf-8"), end=""))
