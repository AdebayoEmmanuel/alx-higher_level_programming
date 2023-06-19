#!/bin/bash
response=$(curl -s -X DELETE $1)
echo "$response"
