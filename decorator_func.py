#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zifengw'

import functools

print('------------------------First one----------------------------')
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-04-03')

now()
print(now.__name__)

print('------------------------Second one----------------------------')
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-04-03')

now()
print(now.__name__)

print('------------------------Exercises----------------------------')
def log(text='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s begin:' % (text, func.__name__))
            ret = func(*args, **kw)
            print('%s %s end:' % (text, func.__name__))
            return ret
        return wrapper
    return decorator

#@log('execute')
@log()
def now():
    print('2017-04-03')

now()

