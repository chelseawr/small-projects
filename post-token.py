#!/bin/python3
import requests
import json

'''
    used as application for software engineer job
    basic POST request to redacted server
    uses a token auth header in base64
    payload contains JSON of contact info
        Chelsea May - 2021    
'''

# base64 Software Engineer - Web
token = 'Bearer U29mdHdhcmUgRW5naW5lZXIgLSBXZWI='

url = '/url/api-post/json-upload'
headers = {'Authorization': token}

data = json.load(open('contactinfo.json',))
print(data)

try:
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print(' Response: ', r, r.text)
except requests.exceptions.RequestException as e:  
    raise SystemExit(e)