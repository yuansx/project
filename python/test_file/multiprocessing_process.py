#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import multiprocessing
import os

def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
    print('process (%s) start...' % os.getpid())
    p = multiprocessing.Process(target=run_proc, args=('my_child',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

