#!/bin/bash
# JSON POST request to a URL passed the first argument and displays response
curl -sX POST -H "Content-Type: application/json" -d @"$2"  "$1"
