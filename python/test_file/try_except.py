#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import logging

try:
    num = input("please input a number: ")
    num = int(num)
    print('1 / %d = %f' % (num, 1 / num))
except ZeroDivisionError as e:
    print('except: ', e)
    logging.exception(e)
except BaseException as e:  # all exception is inherited from BaseException
    print('BaseException: ', e)
    logging.exception(e)
except: # catch all exception by None, but is will catch by last BaseException
    print('Unknow Exception')
else:
    print('nothing has problem!!')
finally:
    print('done')


