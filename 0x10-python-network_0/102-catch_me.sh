#!/bin/bash
# Sends request and cause server to respond
curl -sL -X PUT -H "Origin: Holberton" -d "user_id=98" 0.0.0.0:5000/catch_me