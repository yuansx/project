#!/usr/bin/env python
#-*- coding: utf-8 -*-

from socket import socket, SOCK_STREAM, SOCK_DGRAM, AF_INET
from datetime import datetime
from threading import Thread
import sys, json

def help():
    print('Usage: {0} <tcp|udp> <server|client>'.format(sys.argv[0]))
    sys.exit(0)


class NetworkHandler():
    def __init__(self, b_tcp=True, b_server=True):
        self._type = SOCK_STREAM if b_tcp else SOCK_DGRAM
        self._b_server = b_server
        self._ip = '127.0.0.1'
        self._port = 8888
        self._listen = 1024
        self._handle = None

    def init(self, ip='127.0.0.1', port=8888, listen=100):
        self._ip = ip
        self._port = port
        self._listen = listen
        self._handle = socket(family=AF_INET, type=self._type)
        if self._b_server:
            self._handle.bind((self._ip, self._port))
            self._handle.listen(self._listen)
        print('init {0}......'.format('server' if self._b_server else 'client'))

    def process(self, filename):
        data = {'filename': filename}
        if not self._b_server:
            if self._type == SOCK_STREAM:
                self._handle.connect((self._ip, self._port))
            self._handle.send(json.dumps(data).encode('utf-8'))
            ret = self._handle.recv(1024)
            #print(ret)
            print(json.loads(ret))
            self._handle.close()
        else:
            while True:
                if self._type == SOCK_STREAM:
                    client, addr = self._handle.accept()
                    ret = client.recv(1024)
                    recv_data = json.loads(ret)
                    print(recv_data)
                    recv_data['code'] = 'ok'
                    client.send(json.dumps(recv_data).encode('utf-8'))
                    client.close()
            self._handle.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        help()
    if sys.argv[1].lower() == 'tcp':
        if sys.argv[2].lower() == 'server':
            server = NetworkHandler()
            server.init()
            server.process('thread_socket_test.py')
        elif sys.argv[2].lower() == 'client':
            client = NetworkHandler(b_server=False)
            client.init()
            client.process('thread_socket_test.py')
        else:
            help()
    elif sys.argv[1].lower() == 'udp':
        if sys.argv[2].lower() == 'server':
            pass
        elif sys.argv[2].lower() == 'client':
            pass
        else:
            help()
    else:
        help()

