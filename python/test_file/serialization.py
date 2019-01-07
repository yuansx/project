#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json

d1 = dict(name = 'derek', age = 24, sex = 'boy')
print(json.dumps(d1))
d2 = json.loads('{"name":"Jennie", "age":25, "sex":"girl"}')
print(json.dumps(d2))

L = [d1, d2]
print(json.dumps(L))

class Student(object):
    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self._sex = sex

s = Student('xiao', 22, 'boy')
print(json.dumps(s, default=lambda obj: obj.__dict__))

