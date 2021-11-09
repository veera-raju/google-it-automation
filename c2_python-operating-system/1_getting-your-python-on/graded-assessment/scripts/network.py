#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'
        if check_localhost == localhost:
           return true
        else:
           return false 

def check_connectivity():
    request = requests.get("http://www.google.com")
        if check_connectivity == 200:
            return true 
        else:
            return false
    return 200
