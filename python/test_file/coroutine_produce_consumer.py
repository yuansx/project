#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[Produce] Producing %d...' % n)
        r = c.send(n)
        print('[Produce] Consumer return: %s' % r)
    c.close()

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] Consuming %s...' % n)
        r = '200 OK'

c = consumer()
produce(c)

