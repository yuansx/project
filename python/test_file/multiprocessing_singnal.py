#!/usr/bin/env python
#-*- codding: utf-8 -*-

import multiprocessing
import signal
import os
import time


def exit_for_signal(sig_id, frame):
    os.environ['terminate'] = "true"
    print('{0}: {1} in {2}, terminate {3}'.format(sig_id, frame, os.getpid(), os.getenv('terminate')))

def exit_for_child(sig_id, frame):
    print('recv signal {0} in {1}'.format(sig_id, os.getpid()))
    print(frame.f_lineno)

def ignore_signal(sig_id, frame):
    print('ig {0}: {1} in {2}, terminate {3}'.format(sig_id, frame, os.getpid(), os.getenv('terminate')))

def test():
    signal.signal(signal.SIGINT, ignore_signal)
    for _ in range(2):
        print('test in {0}, terminate {1}'.format(os.getpid(), os.getenv('terminate')))
        time.sleep(1)


if __name__ == '__main__':
    print('run in {0}'.format(os.getpid()))
    signal.signal(signal.SIGTERM, exit_for_signal)
    signal.signal(signal.SIGCHLD, exit_for_child)
    a = multiprocessing.Process(name='test', target=test)
    print(a.is_alive())
    a.start()
    print(a.is_alive())
    a.terminate()
    print(a.is_alive())
    signal.signal(signal.SIGINT, exit_for_signal)
    a.join()
    print(a.is_alive())
    time.sleep(2)

