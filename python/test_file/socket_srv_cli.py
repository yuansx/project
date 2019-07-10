#!/usr/bin/env python
#-*- coding: utf-8 -*-

import socket
import json
import time

HOST = 'localhost'
PORT = 12345
ADDR = (HOST, PORT)
BUFSIZ = 1024

def tcp_server():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(ADDR)
    srv.listen(5)

    while True:
        print('waitting for client connect......')
        cli, addr = srv.accept()
        while True:
            data = cli.recv(BUFSIZ)
            print('recv from ', addr, ' ', data)
            if not data or data == '':
                break
            data = json.loads(data)
            rsp = data
            if data['cmd'] == 'show':
                rsp['status'] = True
                rsp['time'] = time.ctime()
            else:
                rsp['status'] = False
            cli.send(json.dumps(rsp).encode())
        cli.close()
    srv.close()

def tcp_client():
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect(ADDR)
    while True:
        data = input('>')
        print('send ', data)
        if not data or data == 'exit' or data == 'quit' or data == 'q':
            break
        data = {'cmd': 'show', 'data': data}
        cli.send(json.dumps(data).encode())
        data = cli.recv(BUFSIZ)
        if not data:
            break
        print(data)
    cli.close()

if __name__ == '__main__':
    ch = input('input 1 for srv, 2 for cli: ')
    if ch == '1':
        tcp_server()
    elif ch == '2':
        tcp_client()
    else:
        print('input 1 or 2')

