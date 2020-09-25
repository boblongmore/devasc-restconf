#!/usr/bin/env python

import requests
import json

host = "https://192.168.2.161/restconf/data/"

#uri = "Cisco-IOS-XE-native:native/ip/route"
uri = "Cisco-IOS-XE-ospf-oper"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

username = 'wwt'
password = 'WWTwwt1!'

def build_session():

    session = requests.session()
    session.auth = (username, password)
    session.verify = False
    session.headers = headers
    return session

def get_intf():
    url = (host+uri)
    session = build_session()

    results = session.get(url)
    return results.json()

if __name__ == "__main__":
    results = json.dumps(get_intf())
    print(results)

