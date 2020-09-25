#!/usr/bin/env python

import requests
import json

#every restconf call begins with the restconf/data path"
host = "https://192.168.2.161/restconf/data/"

#find the path using pyang, ANX, or yang explorer
path = "Cisco-IOS-XE-native:native/ip/route"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

username = 'wwt'
password = 'WWTwwt1!'

payload = {
  "Cisco-IOS-XE-native:route": {
    "ip-route-interface-forwarding-list": [
      {
        "prefix": "2.2.2.2",
        "mask": "255.255.255.255",
        "fwd-list": [
          {
            "fwd": "192.168.2.2"
          }
        ]
      }
    ]
  }
}

def build_session():

    session = requests.session()
    session.auth = (username, password)
    session.verify = False
    session.headers = headers
    return session

def add_ip_route():
    url = (host+path)
    session = build_session()

    results = session.patch(url, json=payload)
    return results.status_code

if __name__ == "__main__":
    results = add_ip_route()
    print(f"Returned status code {results}")