#!/usr/bin/env python

import requests
import json
import yaml


#every restconf call begins with the restconf/data path"
host = "https://r1.lab.local/restconf/data/"

#find the path using pyang, ANX, or yang explorer
path = "ietf-interfaces:interfaces/interface=Loopback3"

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

def del_intf():
    url = (host+path)
    session = build_session()

    results = session.delete(url)
    return results.status_code

if __name__ == "__main__":
    results = del_intf()
    print(f"returned status code: {results}")