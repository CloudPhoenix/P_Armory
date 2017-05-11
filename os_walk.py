#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

for root, dirs, files in os.walk(r'./dir_test/', topdown=True):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

