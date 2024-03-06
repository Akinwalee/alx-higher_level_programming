#!/bin/bash
# Sends post request wit data from file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
