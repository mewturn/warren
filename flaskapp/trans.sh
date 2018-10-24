#!/bin/bash
message=$1


curl -v -H 'Content-Type: application/json' -X POST -d '[{ "src" : "'"${message:q}"'"}]' http://127.0.0.1:$2/translator/translate 