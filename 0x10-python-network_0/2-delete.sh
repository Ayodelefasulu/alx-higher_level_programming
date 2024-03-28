#!/bin/bash
# This script sends a DELETE request to a URL and displays the body of the response
curl -s -X DELETE "$1" -o response.txt && cat response.txt
