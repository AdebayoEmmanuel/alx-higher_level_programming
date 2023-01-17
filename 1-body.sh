#!/bin/bash
# send GET request and print body of response of only 200 status
$(curl -s -o - -w %{http_code} $1) | (read -r status; [[ $status -eq 200 ]] && tail -n +2)
