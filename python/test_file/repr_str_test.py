#!/usr/bin/env python
#-*- coding: utf-8 -*-


class A(object):
    def __init__(self, name='a'):
        self._name = name

    def __repr__(self):
        print('in repr')
        return '{0}'.format(self._name)
    
    def __str__(self):
        print('in str')
        return '{0}_{1}'.format(self._name, self.__class__.__name__)

if __name__ == '__main__':
    a = A('11')
    print(repr(a))

