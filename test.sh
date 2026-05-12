#!/usr/bin/env bash

if [ "$#" -eq 1 ] && [[ "$1" != *"."* ]]; then
    python3 -m unittest discover -s src -k "$1"
elif [ "$#" -gt 0 ]; then
    python3 -m unittest "$@"
else
    python3 -m unittest discover -s src
fi
