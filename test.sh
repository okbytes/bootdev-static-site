#!/usr/bin/env bash

export PYTHONPATH="src${PYTHONPATH:+:$PYTHONPATH}"

if [ "$#" -eq 2 ] && [[ "$1" == *.py ]] && [[ "$2" != *"."* ]]; then
    module="${1%.py}"
    module="${module//\//.}"
    python3 -m unittest "$module.$2"
elif [ "$#" -eq 1 ] && [[ "$1" != *"."* ]]; then
    python3 -m unittest discover -s src -k "$1"
elif [ "$#" -gt 0 ]; then
    python3 -m unittest "$@"
else
    python3 -m unittest discover -s src
fi
