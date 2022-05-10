#!/usr/bin/env python3
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.gevent import GeventScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.executors.gevent import GeventExecutor
from pytz import utc
from apscheduler.events import *
import signal
import time
import gevent.monkey

terminate = False

def init_scheduler(b_gevent):
    if b_gevent:
        sched = GeventScheduler()
        default = GeventExecutor()
        gevent.monkey.patch_all()
    else:
        sched = BackgroundScheduler()
        default = ThreadPoolExecutor(20)
    executors = {
        'default': default,
        'processpool': ProcessPoolExecutor(5),
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 1,
    }
    sched.configure(executors=executors, job_defaults=job_defaults, timezone=utc)
    return sched

def test(*args, **kwargs):
    print('test')
    time.sleep(5)
    print('done')

def add_job(sched):
    sched.add_job('test_apscheduler:test', trigger='interval', seconds=1, name='test')

def signal_handler(sig_id, frame):
    global terminate
    terminate = True
    print('recv signal {0}'.format(sig_id))

def init_signal():
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

def main():
    sched = init_scheduler(False)
    add_job(sched)
    sched.start()
    init_signal()
    while not terminate:
        time.sleep(1)
    print('out of loop')
    sched.shutdown()

if __name__ == '__main__':
    main()
