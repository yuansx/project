#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import time

def main():
    context = u'深圳欢迎你'
    while True:
        os.system('clear')
        print(context)
        time.sleep(1)
        context = context[1:] + context[0]

if __name__ == '__main__':
    main()

