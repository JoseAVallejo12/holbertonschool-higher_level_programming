#!/usr/bin/python3
"""Use github APi for list the 10 las commit in user and repo given."""
import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[1], sys.argv[2])
    response = requests.get(url)
    data = response.json()
    try:
        for idx in range(10):
            print("{}: {}".format(
                data[idx].get('sha'),
                data[idx].get('commit').get('author').get('name')))
    except IndexError:
        pass
