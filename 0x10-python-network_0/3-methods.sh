#!/bin/bash
# Show all method of the URL argument
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
