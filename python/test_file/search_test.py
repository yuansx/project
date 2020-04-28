#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
from sort_test import merge_sort

def seq_search(_list, key):
    for idx, item in enumerate(_list):
        if item == key:
            return idx
    return -1


def bin_search(_list, key):
    start, end = 0, len(_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > _list[mid]:
            start = mid + 1
        elif key < _list[mid]:
            end = mid - 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    rand_list = random.sample(range(1, 100), 50)
    rand_list = merge_sort(rand_list)
    print(seq_search(rand_list, 26))
    print(bin_search(rand_list, 26))

