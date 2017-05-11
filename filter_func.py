#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

print('--------------First one--------------------')
def is_odd(n):
    return n % 2 == 1

L = range(100)
print(list(filter(is_odd, L)))

print('--------------Second one--------------------')
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', 'B', 'None', 'C', ' '])))

print('--------------Third one--------------------')
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(m):
    return lambda x: x % m > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        print('n is ', n)
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 20:
        print(n)
    else:
        break

print('--------------Fourth one--------------------')
def is_palindrome(n):
    s = str(n)
    return s[::1] == s[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))

