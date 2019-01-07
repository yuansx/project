#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import threading

num = 0
lock = threading.Lock()

def changed_it(n):
    global num
    num += n
    num -= n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            changed_it(n)
        except BaseException as e:
            print('exception: ', e)
        finally:
            lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target = run_thread, args = (2, ))
    t2 = threading.Thread(target = run_thread, args = (5, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)


