#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput

def read_in_chunks(filepath, chunk_size=1024*1024):
    file_path = open(filepath, 'r')
    while True:
        chunk_data = file_path.read(chunk_size)
        if not chunk_data:
            break
        yield chunk_data

def with_open_fd(filepath):
    with open(filepath, 'r') as fd:
        for line in fd:
            print(line)

def file_input_fd(filepath):
    for line in fileinput.input(filepath):
        print(line)

if __name__ == '__main__':
    filepath = 'hello.py'

    #for chunk in read_in_chunks(filepath):
    #    print(chunk)
    
    #with_open_fd(filepath)

    file_input_fd(filepath)

