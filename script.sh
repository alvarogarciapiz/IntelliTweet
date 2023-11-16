#!/bin/bash

FILE_PATH="/Users/alvaro/Library/Mobile Documents/com~apple~CloudDocs/CGA.txt"
SCRIPT_PATH="/Users/alvaro/Documents/Coding/IntelliTweet/main.py"

LAST_MODIFIED=$(stat -f %m "$FILE_PATH")

while true; do
    CURRENT_MODIFIED=$(stat -f %m "$FILE_PATH")

    if [[ "$CURRENT_MODIFIED" != "$LAST_MODIFIED" ]]; then
        if [[ -s "$FILE_PATH" ]]; then
            echo "-------------------------------------------------"
            echo "| NEW URL FOUND                                  |"
            echo "-------------------------------------------------"
            URL=$(cat "$FILE_PATH")

            /usr/bin/python3 -W ignore $SCRIPT_PATH $URL

            > "$FILE_PATH" # Vaciar el archivo
            LAST_MODIFIED=$CURRENT_MODIFIED
            echo "-------------------------------------------------"
            echo "| EMPTY FILE, WAITING FOR THE NEXT ONE :)        |"
            echo "-------------------------------------------------"
        fi
    fi

    sleep 3 # Cambiar esta frecuencia si se desea
done