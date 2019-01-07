#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import threading,time
local_vairable = threading.local()

def run_thread(name):
    global local_vairable
    local_vairable.name = name
    time.sleep(1)
    print('Thread(%s) local name %s' % (threading.current_thread().name, local_vairable.name))

if __name__ == '__main__':
    t1 = threading.Thread(target = run_thread, args = ('derek',), name = 'First')
    t2 = threading.Thread(target = run_thread, args = ('Jennie', ), name = 'Second')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

