#!/usr/bin/env python
#-*- coding: utf-8 -*-

from time import time
from multiprocessing import Process, Queue
from random import randint

MAX_NUM = 10000000

def calc_test1():
    print('----------------------------------------------')
    start = time()
    total = 0
    data = [i for i in range(1, MAX_NUM)]
    mid = time()
    for one in data:
        total += one
    print(total)
    end = time()
    print('Execute time: {0}'.format(end - mid))
    print('Execute total time: {0}'.format(end - start))
    print('----------------------------------------------')

def calc_test2():
    def calc_handler(data, res_queue):
        total = 0
        for one in data:
            total += one
        res_queue.put(total)

    print('----------------------------------------------')
    start = time()
    process_list = []
    res_queue = Queue()
    process_num = 10
    total = 0
    data = [i for i in range(1, MAX_NUM)]
    step = int(len(data) / process_num) + 1
    mid1 = time()
    for i in range(0, len(data), step):
        p = Process(target=calc_handler, args=(data[i : i + step], res_queue))
        p.start()
        process_list.append(p)
    mid2 = time()
    for p in process_list:
        p.join()
    while not res_queue.empty():
        total += res_queue.get()
    print(total)
    end = time()
    print('Execute pre process time: {0}'.format(end - mid1))
    print('Execute time: {0}'.format(end - mid2))
    print('Execute total time: {0}'.format(end - start))
    print('----------------------------------------------')

if __name__ == '__main__':
    calc_test1()
    calc_test2()

