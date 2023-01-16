#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and A header variable X-School-User-Id must be sent with the value 98
curl -s "$1" -X GET -H "X-School-User-Id: 98"
