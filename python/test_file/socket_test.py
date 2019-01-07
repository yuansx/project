#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com', 80))
s.send(b'GET / HTTP1.1\r\nHost: www.sina.com\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
s.close()
data = b''.join(buffer)
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
print(html)

