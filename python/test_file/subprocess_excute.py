#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import subprocess

r = subprocess.call(['nslookup', 'www.tencent.com'])
print('Exit code: ', r)

print('------------分割线-------------')

p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output, err = p.communicate(b'set q=mx\nwww.baidu.com\nexit\n')
print(output.decode('gbk'))
print('Exit code: ', p.returncode)

