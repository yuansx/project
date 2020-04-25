#!/usr/bin/env python
#-*- coding:utf-8 -*-

from multiprocessing import Process
from threading import Thread
from os import getpid
from random import randint
from time import time, sleep

def learning(num, method='process'):
    print('{0} start learning by {1} at {2}'.format(num, method, getpid()))
    sleep(1)
    #sleep(randint(1, 5))
    print('{0} end learning at {1}'.format(num, getpid()))


def thread_test():
    start = time()
    thread_list = list()
    for a in range(10):
        t = Thread(target=learning, args=(a, 'thread'))
        t.start()
        thread_list.append(t)
    mid = time()
    print('learning ending by thread, create using {0} seconds'.format(mid - start))
    for t in thread_list:
        t.join()
    end = time()
    print('learning ending by thread, using {0} seconds'.format(end - start))


def process_test():
    start = time()
    process_list = list()
    for a in range(10):
        p = Process(target=learning, args=(a,))
        p.start()
        process_list.append(p)
    mid = time()
    print('learning ending by process, create using {0} seconds'.format(mid - start))
    for p in process_list:
        p.join()
    end = time()
    print('learning ending by process, using {0} seconds'.format(end - start))


class Study(Thread):
    def __init__(self, num):
        super().__init__()
        self._num = num

    def run(self):
        learning(self._num, 'thread_class')

def study_test():
    start = time()
    class_list = list()
    for a in range(10):
        s = Study(a)
        s.start()
        class_list.append(s)
    mid = time()
    print('learning ending by thread class, create using {0} seconds'.format(mid - start))
    for s in class_list:
        s.join()
    end = time()
    print('learning ending by thread class, using {0} seconds'.format(end - start))

if __name__ == '__main__':
    process_test()
    thread_test()
    study_test()

