#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code
curl -s -X GET "$1" -o response.txt && grep -i "200 OK" response.txt && cat response.txt
