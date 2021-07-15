#!/usr/bin/env python
#-*- codding: utf-8 -*-

from multiprocessing import Queue

def main():
    q = Queue(10)
    q.put(1)
    q.put('a')
    print(q.qsize())
    print(q.full())
    q.get()
    q.get()
    print(q.empty())
    q.get(timeout=2)


if '__main__' == __name__:
    main()

