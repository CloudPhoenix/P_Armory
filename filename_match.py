#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def _find_alldirs(path):
    dirs_list = [os.path.join(path,x) for x in os.listdir(path) \
            if os.path.isdir(os.path.join(path,x))]
    if dirs_list:
        print(dirs_list)
        [_find_alldirs(x) for x in dirs_list]

def filename_match1(path, str_match):
    if os.path.isdir(path):
        files_list = [os.path.join(path, x) for x in os.listdir(path) \
                if os.path.isfile(os.path.join(path, x)) and str_match in x]
        if files_list:
            print(files_list)
        dirs_list = [os.path.join(path,x) for x in os.listdir(path) \
                if os.path.isdir(os.path.join(path,x))]
        if dirs_list:
            [filename_match1(x, str_match) for x in dirs_list]

def filename_match2(path, str_match):
    files_list = [os.path.join(path,x) for x in os.listdir(path) \
            if os.path.isfile(os.path.join(path,x))]
    dirs_list = [os.path.join(path,x) for x in os.listdir(path) \
            if os.path.isdir(os.path.join(path,x))]
    if files_list:
        for file_str in files_list:
            if str_match in file_str:
                print(os.path.join(path,file_str))
    if dirs_list:
        for dir_str in dirs_list:
            filename_match2(os.path.join(path,dir_str), str_match)

def str_match_print1(path, str_match):
    files_list = [os.path.join(path,x) for x in os.listdir(path) \
            if os.path.isfile(os.path.join(path,x))]
    dirs_list = [os.path.join(path,x) for x in os.listdir(path) \
            if os.path.isdir(os.path.join(path,x))]
    if files_list:
        for file_str in files_list:
            if str_match in file_str:
                path_str = os.path.join(path,file_str)
                with open(path_str, 'r') as fd_path:
                    print(fd_path.read())
    if dirs_list:
        for dir_str in dirs_list:
            str_match_print1(os.path.join(path,dir_str), str_match)

def str_match_print2(path, str_match):
    if os.path.isdir(path):
        files_list = [os.path.join(path, x) for x in os.listdir(path) \
                if os.path.isfile(os.path.join(path, x)) and str_match in x]
        dirs_list = [os.path.join(path,x) for x in os.listdir(path) \
                if os.path.isdir(os.path.join(path,x))]
        if files_list:
            yield files_list
        if dirs_list:
            [str_match_print2(x, str_match) for x in dirs_list]

if __name__ == '__main__':
    #_find_alldirs(r'e:\devspace\python\dir_test')
    #filename_match1(r'e:\devspace\python\dir_test', '.py')
    #filename_match2(r'e:\devspace\python\dir_test', '.py')
    #str_match_print1(r'e:\devspace\python\dir_test', '.py')
    path_G = str_match_print2(r'e:\devspace\python\dir_test', '.py')
    for path_str in path_G:
        print(path_str)
        #with open(path_str, 'r') as fd_path:
        #    print(fd_path.read())


