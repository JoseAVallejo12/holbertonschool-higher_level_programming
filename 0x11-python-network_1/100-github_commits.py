#!/usr/bin/python3
"""Use github APi for list the 10 las commit in user and repo given."""
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    repo = sys.argv[2]
    response = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(
            user, repo))
    data = response.json()
    for idx in range(10):
        print("{}: {}".format(
            data[idx].get('sha'),
            data[idx].get('commit').get('author').get('name')))
