#!/bin/bash
# Show all method of the URL argument
curl -IX OPTIONS "$1" | grep -i '^allow: ' | cut -d ':' -f 2-
