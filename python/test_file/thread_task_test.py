#!/usr/bin/env python
#-*- coding: utf-8 -*-

from time import time
from multiprocessing import Process, Queue
from random import randint

def calc_test1():
    start = time()
    total = 0
    data = [i for i in range(1, 100000000)]
    for one in data:
        total += one
    print(total)
    end = time()
    print('Execute time: {0}'.format(end - start))

def calc_test2():
    def calc_handler(data, res_queue):
        total = 0
        for one in data:
            total += one
        res_queue.put(total)

    start = time()
    process_list = []
    res_queue = Queue()
    process_num = 10
    total = 0
    data = [i for i in range(1, 100000000)]
    step = int(len(data) / process_num) + 1
    for i in range(0, len(data), step):
        p = Process(target=calc_handler, args=(data[i : i + step], res_queue))
        p.start()
        process_list.append(p)
    for p in process_list:
        p.join()
    while not res_queue.empty():
        total += res_queue.get()
    print(total)
    end = time()
    print('Execute time: {0}'.format(end - start))

if __name__ == '__main__':
    calc_test1()
    calc_test2()

