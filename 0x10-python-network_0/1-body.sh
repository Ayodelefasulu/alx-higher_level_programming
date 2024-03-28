#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code
curl -s -o response.txt -w "%{http_code}" "$1" | grep -q "200" && cat response.txt
