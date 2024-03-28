#!/bin/bash
# Display body for successful (200) GET request
curl -s "$1" | grep -Ev '^HTTP.*$' | grep -Ev '^$'
