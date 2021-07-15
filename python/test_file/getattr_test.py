#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys


class A():
    def a(self):
        print('aa')

    def b(self):
        print('bb')


if __name__ == '__main__':
    a = A()
    func = 'a'
    getattr(a, func)()

