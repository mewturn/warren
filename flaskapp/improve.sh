#!/bin/bash

mysql --host=35.229.167.44 -u root -p1234567890 -e "INSERT INTO improvements.corpus (\`en\`, \`zh-hant\`, \`improved\`) VALUES ('$1', '$2', '$3');"