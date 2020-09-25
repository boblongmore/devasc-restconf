#!/usr/bin/env python

import requests
import json


#every restconf call begins with the restconf/data path"
host = "https://r1.lab.local/restconf/data/"

#find the path using pyang, ANX, or yang explorer
path = "ietf-interfaces:interfaces/"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

#builds the request to get interfaces currently configured on the router
#returns those results in json format
def get_intf():
    url = (host+path)
    results = requests.get(url, auth = ('wwt', 'WWTwwt1!'), headers=headers, verify=False)
    return results.json()

if __name__ == "__main__":
    results = json.dumps(get_intf(), indent=2)
    print(results)
