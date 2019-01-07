#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while (n < max):
        print(b)
        a, b = b, a + b
        n += 1
    print('done')

def fib_yield(max):
    n, a, b = 0, 0, 1
    while (n < max):
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

fib(6)
print('---------分割线----------')
L = fib_yield(6)
for n in L:
    print(n)
print('---------分割线----------')
L = fib_yield(6)
while True:
    try:
        n = next(L)
        print(n)
    except StopIteration as e:
        print(e.value)
        break

