#!/bin/bash
# Display body of 200 response from URL
curl -s -w "%{http_code}" "$1" -o /dev/null | grep 200 >/dev/null && curl -s "$1"
