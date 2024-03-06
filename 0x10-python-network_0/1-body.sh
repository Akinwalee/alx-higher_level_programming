#!/usr/bin/env bash
#Script that sends a GET request to a server and prints the body if success

if [ -z "$1" ]; then
	exit 1
fi

headers=$(curl -sLI "$1")
response=$(curl -sLf "$1")

s_code=$(echo "$headers" | grep -oP 'HTTP\/\d\.\d\s200')

echo 
if [ "$s_code" != 200 ]; then
	echo "$s_code"
	exit 1
fi

echo "$response"
