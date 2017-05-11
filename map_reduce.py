#!/usr/bin/env python3

from functools import reduce

print('-------------First one:-----------------')
def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('-------------Second one:-----------------')
def prod(L):
    return reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

print('-------------Third one:-----------------')

def char2num(s):
    return {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2float(str):
    L = str.split('.')
    return reduce(lambda x, y: x * 10 + y, map(char2num, L[0])) + \
    reduce(lambda x, y: x * 0.1 + y, map(char2num, L[1][::-1])) * 0.1

print('str2float(\'123.456\')=', str2float('123.456'))

