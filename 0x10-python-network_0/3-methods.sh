#!/bin/bash
# This script retrieves and displays all HTTP methods accepted by the server for a given URL
curl -s -X OPTIONS -i "$1" | grep -i Allow | cut -d':' -f2- | tr -d '\r\n'
