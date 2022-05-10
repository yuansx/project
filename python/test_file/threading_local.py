#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import threading,time
local_vairable = threading.local()

def run_thread(name):
    global local_vairable
    local_vairable.name = name
    time.sleep(1)
    print('Thread(%s) local name %s' % (threading.current_thread().name, local_vairable.name))


class MyThread(threading.Thread):
    def __init__(self, name, scores):
        threading.Thread.__init__(self)
        self.name = name
        self.scores = scores

    def run(self):
        local_vairable.name = self.name
        local_vairable.scores = self.scores
        for i in range(10):
            idx = 0 if local_vairable.name == 'derek' else 1
            local_vairable.scores[idx] -= 1
            print('name: {0}, scores({1}): {2}'.format(local_vairable.name, id(local_vairable.scores), local_vairable.scores))
            time.sleep(1)


def simple_test_local():
    t1 = threading.Thread(target = run_thread, args = ('derek',), name = 'First')
    t2 = threading.Thread(target = run_thread, args = ('Jennie', ), name = 'Second')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def test_local():
    scores = [100, 100, 100]
    t1 = MyThread('derek', scores)
    t2 = MyThread('jennie', scores)
    t1.start()
    t2.start()
    for i in range(5):
        scores[2] -= 1
        print('name: main, scores({0}): {1}'.format(id(scores), scores))
        time.sleep(1)
    t1.join()
    t2.join()

if __name__ == '__main__':
    test_local()

