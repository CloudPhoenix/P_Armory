#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Perform Yang Hui triangles.

__author__ = 'zifengw'

def YH_triangles():
    L = [1,]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

if __name__ == '__main__':
    count = 0
    for t_line in YH_triangles():
        print(t_line)
        count += 1
        if count == 10:
            break

