#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from multiprocessing.managers import BaseManager
import multiprocessing
import os
import time


class QueueManager(BaseManager):
    pass

def run_proc(name):
    print(dir(QueueManager))
    print('Run child process %s (%s)' % (name, os.getpid()))
    time.sleep(10)

if __name__ == '__main__':
    print('process (%s) start...' % os.getpid())
    q = multiprocessing.Queue()
    QueueManager.register('get_queue', callable=lambda: q)
    p = multiprocessing.Process(target=run_proc, args=('my_child',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

