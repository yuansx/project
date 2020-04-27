#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
import sys

def select_sort(data, comp=lambda x, y: x < y):
    cycle_cnt = 0
    cmp_cnt = 0
    assign_cnt = 0
    data = data[:]
    for i in range(len(data) - 1):
        min_idx = i
        for j in range(i + 1, len(data)):
            cycle_cnt += 1
            if comp(data[j], data[min_idx]):
                cmp_cnt += 1
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        assign_cnt += 1
    print('{0}: cycle: {1}, cmp: {2}, assign: {3}'.format(sys._getframe().f_code.co_name, cycle_cnt, cmp_cnt, assign_cnt))
    return data


def bubble_sort(data, comp=lambda x, y: x < y):
    cycle_cnt = 0
    cmp_cnt = 0
    assign_cnt = 0
    data = data[:]
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            cycle_cnt += 1
            if comp(data[j], data[i]):
                cmp_cnt += 1
                assign_cnt += 1
                data[i], data[j] = data[j], data[i]
    print('{0}: cycle: {1}, cmp: {2}, assign: {3}'.format(sys._getframe().f_code.co_name, cycle_cnt, cmp_cnt, assign_cnt))
    return data


if __name__ == '__main__':
#    rand_list = [random.randint(1, 100) for i in range(10)]
    rand_list = random.sample(range(1, 100), 10)
    print(rand_list)
    print(select_sort(rand_list))
    print(bubble_sort(rand_list))

