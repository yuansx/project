#!/usr/bin/env python
#-*- coding: utf-8 -*-

from socket import socket, SOCK_STREAM, SOCK_DGRAM, AF_INET
from datetime import datetime
from threading import Thread
import sys, json, os, time

def help():
    print('Usage: {0} <tcp|udp> <server|client>'.format(sys.argv[0]))
    sys.exit(0)

class WorkerHandler(Thread):
    def __init__(self, client, addr):
        super().__init__()
        self._client = client
        self._addr = addr

    def run(self):
        print('{0} is connect......'.format(self._addr))
        time.sleep(10)
        buf = bytes()
        ret = self._client.recv(1024)
        while ret:
            buf += ret
            print('recv {0}'.format(buf))
            if len(ret) < 1024:
                break
            ret = self._client.recv(1024)
        try:
            data = json.loads(buf)
        except:
            print('recv data is not a json string')
            return
        if 'filename' not in data or 'method' not in data or not isinstance(data['filename'], str) or not isinstance(data['method'], str):
            print('Invalid format of recv data {0}'.format(data))
            return
        if data['method'].lower() not in ('read', 'append', 'exists'):
            print('Invalid format of method({0}) in recv data'.format(data['method']))
            return
        if data['method'].lower() == 'read':
            mode = os.F_OK | os.R_OK
        elif data['method'].lower() == 'write':
            mode = os.F_OK | os.W_OK
        else:
            mode = os.F_OK
        if not os.access(data['filename'], mode):
            print('file {0} can not {1}'.format(data['filename'], data['method']))
            return
        if data['method'] == 'read':
            with open(data['filename'], 'r') as f:
                data['rsp'] = f.read()
        elif data['method'] == 'exists':
            data['rsp'] = 'file {0} is exists'.format(data['filename'])
        self._client.send(json.dumps(data).encode('utf-8'))
        self._client.close()


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

    def process(self, filename=None, method=None):
        if not self._b_server:
            if not filename or not method:
                print('client need to send data')
                return
            data = {'filename': filename, 'method': method}
            if self._type == SOCK_STREAM:
                self._handle.connect((self._ip, self._port))
            self._handle.send(json.dumps(data).encode('utf-8'))
            buf = bytes()
            ret = self._handle.recv(1024)
            while ret:
                buf += ret
                if len(ret) < 1024:
                    break
                ret = self._handle.recv(1024)
            rsp = json.loads(buf.decode('utf-8'))
            print('rsp {0}'.format(rsp['rsp']))
            #print(buf)
            self._handle.close()
        else:
            while True:
                if self._type == SOCK_STREAM:
                    client, addr = self._handle.accept()
                    WorkerHandler(client, addr).start()
                else:
                    WorkerHandler(self._handle, None).start()
            self._handle.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        help()
    if sys.argv[1].lower() == 'tcp':
        if sys.argv[2].lower() == 'server':
            server = NetworkHandler()
            server.init()
            server.process()
        elif sys.argv[2].lower() == 'client':
            client = NetworkHandler(b_server=False)
            client.init()
            client.process('process_test.py', 'read')
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

