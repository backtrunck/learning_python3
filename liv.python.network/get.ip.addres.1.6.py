#!/usr/bin/env python3

import socket
hostname = 'maps.google.com'
addr = socket.gethostbyname(hostname)

print('the address of',hostname,'is ',addr)

