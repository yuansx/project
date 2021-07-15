#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing.managers import BaseManager
from multiprocessing import Queue
import queue
import os
from random import randint


PORT = 7070


class QueueManager(BaseManager):
    pass


def server():
    task_queue = Queue()
    result_queue = Queue()
    QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register('get_result_queue', callable=lambda: result_queue)
    manager = QueueManager(address=('', PORT), authkey=b'derek')
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(10):
        n = randint(0, 10000)
        print(n)
        task.put(n)
    for i in range(10):
        r = result.get(timeout=10)
        print(r)
    manager.shutdown()


def worker(server_ip='127.0.0.1'):
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    q = QueueManager(address=(server_ip, PORT), authkey=b'derek')
    q.connect()
    task = q.get_task_queue()
    result = q.get_result_queue()
    while True:
        try:
            n = task.get(timeout=1)
            print(n)
            result.put('{0} + {1} = {2}'.format(n, n, n + n))
        except queue.Empty:
            print('task queue is empty')
            break
        except EOFError:
            print('task queue is shutdown')
            break


if __name__ == '__main__':
    print(os.path.split(os.path.realpath(os.sys.argv[0]))[0])
    print(os.getcwd())
    if len(os.sys.argv) == 2:
        worker(os.sys.argv[1])
    else:
        server()
