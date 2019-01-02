#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import collections

L1 = ['hello', 'woRld', 18, 'appLe', None]

print([n.title() for n in L1 if isinstance(n, str)])

print('list is iterable: ' + str(isinstance(L1, collections.Iterable)))
print('list is iterator: ' + str(isinstance(L1, collections.Iterator)))


