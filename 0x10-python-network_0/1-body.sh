#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code
curl -s -w "%{http_code}" -o response.txt "$1"; status_code=$(tail -n1 response.txt); [[ $status_code == "200" ]] && cat response.txt
