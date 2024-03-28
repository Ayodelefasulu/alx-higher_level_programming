#!/bin/bash
# Display body for successful (200) GET request (alternative)
if [[ $(curl -s -o /dev/null -w "%{http_code}" "$1") == 200 ]]; then curl -s "$1"; fi
