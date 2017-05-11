#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reverse_word_sentence1(words_str):
    words_list = words_str.split()
    words_list = words_list[::-1]
    print(' '.join(words_list))

def reverse_word_sentence2(words_str):
    i_index = j_index = len(words_str) - 1
    words_tmp = ''
    while i_index >0 and j_index > 0:
        if words_str[j_index] != ' ':
            j_index -= 1
        else:
            words_tmp = words_tmp + ' ' + words_str[(j_index + 1):(i_index + 1)]
            i_index = j_index
            j_index -= 1
    if j_index == 0:
        words_tmp = words_tmp + ' ' + words_str[(j_index):(i_index + 1)]
    print(words_tmp)


if __name__ == '__main__':
    words_str = 'welcome to Beijing'
    #reverse_word_sentence1(words_str)
    reverse_word_sentence2(words_str)


