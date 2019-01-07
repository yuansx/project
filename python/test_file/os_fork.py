#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())

pid = fork()
if pid == 0:
    print('Child process (%s) and Parent (%s)' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s)' % (os.getpid(), pid))

