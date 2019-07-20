#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from random import randint

def rand_num(max_num = 100):
    return randint(1, max_num)


def input_yes_no(tips):
    while True:
        guess = input(tips).lower()
        if guess != 'yes' and guess != 'no':
            print('input yes or no')
        else:
            break
    return guess


def input_num(tips):
    while True:
        num = input(tips)
        if num.isdigit():
            break
    return int(num)
            

def guess_num():
    while True:
        guess = input_yes_no('do you want to guess a num(yes or no): ')
        if guess is 'no':
            break
        num = rand_num()
        while True:
            guess_num = input_num('guess num: ')
            if guess_num > num:
                print('smaller than ', guess_num)
            elif guess_num < num:
                print('larger than ', guess_num)
            else:
                print('you are right, the num is ', num)
                break
        guess = input_yes_no('do you want to try again(yes or no): ')
        if guess == 'no':
            return

if __name__ == '__main__':
    guess_num()


