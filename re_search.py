#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'\d+')

m = pattern.search('hello 123456 789')

if m:
    print('Matching string: ', m.group())
    print('Position: ', m.span())

