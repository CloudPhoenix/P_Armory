#!/usr/bin/env python3

import logging
logging.basicConfig(level=logging.INFO)

import pdb

print('--------------First one-------------------------')
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('Invalid value: %s' % s)
    return 10/n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

#bar()

print('-------------Second one-----------------------')
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10/n

def main():
    foo('0')

#main()

#print('-----------Third one-----------------------------')
#s = '0'
#n = int(s)
#logging.info('n = %d' % n)
#print(10 / n)

print('-----------Fourth one-----------------------------')
s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)

