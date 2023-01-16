#!/bin/bash
# add new things with keys and values
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
