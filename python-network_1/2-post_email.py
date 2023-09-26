#!/usr/bin/ptn3
"""Docmuntation of import"""
import requests
import sys
url=sys.argv[1]
email=sys.argv[2]
playload = {'email':email}
"""post request send"""
r=requests.post(url,data=playload)
return r.text
