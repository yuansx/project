#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from random import randint

def generate_code(n = 4):
    if not isinstance(n , int):
        print('n must be a number')
        return 0
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(n):
        idx = randint(0, len(all_chars))
        code += all_chars[idx]

    return code


def main():
    print(generate_code(int(input('input a number: '))))

if __name__ == '__main__':
    main()

