#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# YiduCloud.com
# Perform the shuffle function

__author__ = 'zifengw'

import random

def w_shuffle(L):
    L_tmp = []
    for num in range(54):
        tmp = L[random.choice(range(54 - num))]
        L.pop(L.index(tmp))
        L_tmp.append(tmp)

    return L_tmp

if __name__ == '__main__':
    L = list(range(54))
    L_shuffle = w_shuffle(L)
    print(L_shuffle)

