#!/usr/bin/env bash
#Script that sends a request to a server and prints the response lenght in bytes

if [ -z "$1" ]; then
	exit 1
fi

response=$(curl -sI "$1")
c_length=$(echo "$response" | grep -i 'content-length:' | awk '{print $2}' | tr -d '\r')

echo "$c_length"
