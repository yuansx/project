#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import datetime
import functools

def log(func):
    @functools.wraps(func)  # swap to the real name of function and ect.
    def wrapper(*args, **kw):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '|%s' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def say_hello():
    print('hello')

say_hello()
print('say_hello.__name__: %s' % say_hello.__name__)

del log
del say_hello


def log(text):
    def decorator(func):
        @functools.wraps(func)  # swap to the real name of function and ect.
        def wrapper(*args, **kw):
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '|%s|%s' % (func.__name__, text))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('expansion: ')
def say_hello():
    print('hello')

say_hello()
print('say_hello.__name__: %s' % say_hello.__name__)
