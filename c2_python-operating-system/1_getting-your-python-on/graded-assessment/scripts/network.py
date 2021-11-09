#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
        print(localhost)
   if check_localhost == print(localhost):
        return true
   else:
        return  false
def check_connectivity():
    request = requests.get("http://www.google.com")
    print(request)
    print(request.status_code)
    if check_connectivity == 200:
        return true 
    else:
        return false
