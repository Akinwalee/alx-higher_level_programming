#!/bin/bash
#Script that sends a request to a server and prints the response lenght in bytes

curl -s "$1" | wc -c
