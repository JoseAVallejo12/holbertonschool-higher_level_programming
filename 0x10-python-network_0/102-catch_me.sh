#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl 0.0.0.0:5000/catch_me -X PUT -sL -d"user_id=98" -H"Origin: HolbertonSchool"
