#!/usr/bin/env python
#-*- coding: utf-8 -*-

import socket
import json

HOST = 'localhost'
PORT = 12345
ADDR = (HOST, PORT)
BUFSIZ = 1024

def tcp_server():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(ADDR)
    srv.listen(5)

    while True:
        cli, addr = srv.accept()
        data = cli.recv(BUFSIZ)
        if not data:
            continue
        print('recv from ', addr, ' ', data)
        cli.send('recv that'.encode())
        cli.close()
    srv.close()

def tcp_client():
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect(ADDR)
    while True:
        data = input('>')
        if not data:
            break
        cli.send(data.encode())
        data = cli.recv(BUFSIZ)
        if not data:
            break
        print(data)
    cli.close()

if __name__ == '__main__':
    ch = input('input 1 for srv, 2 for cli: ')
    if ch == '1':
        tcp_server()
    else:
        tcp_client()

