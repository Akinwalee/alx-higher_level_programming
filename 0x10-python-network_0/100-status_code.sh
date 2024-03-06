#!/bin/bash
# Shows status code only
curl -s -o /dev/nul -w "%{http_code}" "$1"
