#!/bin/python3 

import requests
import json

url="https://api.cloudflare.com/client/v4/zones/"+ZONE_ID+"/logpush/edge/jobs"


data = {"fields":"ClientIP,ClientRequestHost,ClientRequestMethod,ClientRequestURI,EdgeEndTimestamp,EdgeResponseBytes,EdgeResponseStatus,EdgeStartTimestamp,RayID","sample":1,"filter":"","kind":"instant-logs"}

res = requests.post(url, headers=headers, json=data)
response = res.json()

websocataddress=response["result"]["destination_conf"]
import os
print(websocataddress)
os.system("./wsocat "+websocataddress +" >> cloudlfare.json")
