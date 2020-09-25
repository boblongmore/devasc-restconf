#!/usr/bin/env python

import requests
import json
import yaml


#every restconf call begins with the restconf/data path"
host = "https://r1.lab.local/restconf/data/"

#find the path using pyang, ANX, or yang explorer
path = "ietf-interfaces:interfaces/"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

username = "wwt"
password = "WWTwwt1!"

#using requests session to persist session
def build_session():

    session = requests.session()
    session.auth = (username, password)
    session.verify = False
    session.headers = headers
    return session

def build_payload():
    with open ("interfaces.yml", "r") as handle:
        intf_inv = yaml.safe_load(handle)
        print(json.dumps(intf_inv, indent=2))
        return intf_inv

def add_intf():
    url = (host+path)
    session = build_session()
    payload = build_payload()

    results = session.post(url, json=payload)
    return results.status_code

if __name__ == "__main__":
    results = add_intf()
    print(f"returned status code: {results}")