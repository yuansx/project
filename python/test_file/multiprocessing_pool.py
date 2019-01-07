#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import multiprocessing
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    print('Start process %s pool' % os.getpid())
    p = multiprocessing.Pool(multiprocessing.cpu_count())
    for i in range(multiprocessing.cpu_count() + 1):
        p.apply_async(long_time_task, args = (i, ))
    print('Wait for all subprocess done...')
    p.close()
    p.join()
    print('all subprocess done')

