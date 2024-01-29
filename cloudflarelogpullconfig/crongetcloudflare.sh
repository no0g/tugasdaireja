#!/bin/bash

# kill existing socat
pkill wsocat

# run python lagoi
python3 ./getcloudflare.py
