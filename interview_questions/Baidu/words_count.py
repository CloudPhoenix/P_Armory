#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'zifengw'

def words_count():
    with open('words_count.txt', 'r') as inner_file:
        words_str = inner_file.read()
        words_list = words_str.split(' ')

        words_set = set(words_list)
        words_frequency = {}
        words_dict = dict.fromkeys(words_set, 0)
        for key in words_list:
            words_dict[key] = words_dict[key] + 1

        max_frequency = max(words_dict.values())
        print('The max frequency: %d' % max_frequency)

        print('The max keys: ')
        for key in words_set:
            if words_dict[key] == max_frequency:
                print(key)

def word_count():
    file_inner = open("words_count.txt", 'r')
    word_lists = file_inner.read()
    word_list=word_lists.split(' ')
    dic={}
    max=0
    for word in word_list:
        if dic.get(word, -1) == -1:
            dic[word] = 1
        else:
            dic[word] = dic[word] + 1
    for key, value in dic.items():
        if dic[key] > max:
            max = dic[key]
            marked_key = key
    print(marked_key, max)

    #keywords_sorted = sorted(dic.items(), key=lambda d: d[1])
    #print keywords_sorted
    file_inner.close()

if __name__ == '__main__':
    #find_frequency()
    words_count()

