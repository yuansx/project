#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Thing(object):
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        return self.price / self.weight


def input_thing():
    name_str, price_str, weight_str = input('input thing like \'name price weight\': ').split()
    return name_str, int(price_str), int(weight_str)


def greedy_test():
    max_weight, num_of_things = map(int, input('input max weight of knapsack and num of things: ').split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'take {thing.name}')
            total_price += thing.price
            total_weight += thing.weight
    print(f'总价值: {total_price}美元')
    print(f'总重量：{total_weight}kg')


if __name__ == '__main__':
    greedy_test()

