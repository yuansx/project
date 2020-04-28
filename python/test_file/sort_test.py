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


def merge_sort(data, comp=lambda x, y: x < y):
    def _merge_list(list_left, list_right, _comp):
        idx_l = 0
        idx_r = 0
        _list = []
        while idx_l < len(list_left) and idx_r < len(list_right):
            if _comp(list_left[idx_l], list_right[idx_r]):
                _list.append(list_left[idx_l])
                idx_l += 1
            else:
                _list.append(list_right[idx_r])
                idx_r += 1
        _list += list_left[idx_l:]
        _list += list_right[idx_r:]
        return _list

    def _merge_sort(_list, _comp):
        if len(_list) < 2:
            return _list
        mid = len(_list) // 2
        list_left = _merge_sort(_list[:mid], comp)
        list_right = _merge_sort(_list[mid:], comp)
        return _merge_list(list_left, list_right, _comp)

    return _merge_sort(data[:], comp)


if __name__ == '__main__':
#    rand_list = [random.randint(1, 100) for i in range(10)]
    rand_list = random.sample(range(1, 100), 10)
    print(rand_list)
    print(select_sort(rand_list))
    print(bubble_sort(rand_list))
    print(merge_sort(rand_list))

