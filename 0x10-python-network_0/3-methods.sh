#!/bin/bash
# This script retrieves and displays all HTTP methods accepted by the server for a given URL
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{ print $2 }'
