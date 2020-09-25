#!/usr/bin/env python

import requests
import json

host = "https://192.168.2.161/restconf/data/"

path = "openconfig-interfaces:interfaces"

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

def get_ip_route():
    url = (host+path)
    session = build_session()

    results = session.get(url)
    return results.json()

if __name__ == "__main__":
    results = get_ip_route()
    #uncomment to see entire payload
    print(json.dumps(results, indent=2))
    #    print(f"{route['prefix']:17}{route['mask']:17}{route['fwd-list'][0]['fwd']}")
