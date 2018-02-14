#!/usr/bin/env python3
#mande um grande pacote udp para o servidor

import IN, socket, sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

MAX = 65535
PORT = 1060

if len(sys.argv) != 2:
    print('uso: big_sender.py host',file=sys.stderr)
    sys.exit(2)

hostname = sys.argv[1]

s.connect((hostname,PORT))
s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)

try:
    s.send(b'#' * 65500)
except socket.error:
    print('The message did not make it')
    option = getattr(IN,'IP_MTU',14) #constant taken from <linux/in.h>
    print('MTU: ',s.getsockopt(socket.IPPROTO_IP,option))
else:
    print('The big message was sent! Your network supports really big packets')

