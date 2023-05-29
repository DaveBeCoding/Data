#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Error: No file name provided."
    exit 1
fi

filename=$1

# Define the ANSI escape code for the brighter color
BRIGHT_COLOR='\033[1;33m'
# Define the ANSI escape code to reset the color
RESET_COLOR='\033[0m'

# Run the grep command and apply the color to the matched text using sed
grep -E ":[4-9]|[1-9][0-9]+" "$filename" | sed -E "s/(.*:)([0-9]+)/\1$BRIGHT_COLOR\2$RESET_COLOR/g"

