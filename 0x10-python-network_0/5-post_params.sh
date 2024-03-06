#!/bin/bash
# Sends POST request with 2 parameters
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
