#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Screen(object):
    def __init__(self):
        self._width = 0
        self._height = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer!")
        elif value < 0:
            raise TypeError('width must be bigger than 0!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer!')
        elif value < 0:
            raise TypeError('height must be bigger than 0!')
        self._height = value

    @property
    def area(self):
        return self._width * self._height

s = Screen()
s.width = 5
s.height = 6
print("width = %d, height = %d, area = %d" % (s.width, s.height, s.area));

