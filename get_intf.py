#!/usr/bin/env python

import requests
import json

host = "https://r1.lab.local/restconf/data/"

uri = "ietf-interfaces:interfaces/"

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
    results = json.dumps(get_intf(), indent=2)
    print(results)
