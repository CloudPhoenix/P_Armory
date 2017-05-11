#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import subprocess

def word_match_py():
    with open('index.html', 'r') as fd_index:
        for index_line in fd_index:
            flag_group, flag_command = 0, 0
            words_list = index_line.split("'")
            with open('group.c', 'r') as fd_group:
                for group_line in fd_group:
                    if bool(re.search(words_list[3], group_line, re.IGNORECASE)) is True:
                        flag_group += 1
            with open('command.c', 'r') as fd_command:
                for command_line in fd_command:
                    if bool(re.search(words_list[3], command_line, re.IGNORECASE)) is True:
                        flag_command += 1
            if flag_group == 0 and flag_command == 0:
                print(words_list[3],words_list[1])
            else:
                print("No this word.")

def word_match_sh():
    with open('index.html', 'r') as fd_index:
        for index_line in fd_index:
            words_list = index_line.split("'")
            group_cmd = 'grep -i {} group.c'.format(words_list[3])
            command_cmd = 'grep -i {} command.c'.format(words_list[3])
            group_status, group_output = subprocess.getstatusoutput(group_cmd)
            command_status, command_output = subprocess.getstatusoutput(command_cmd)
            if group_status > 0 and command_status > 0:
                print(words_list[3], words_list[1])

if __name__ == '__main__':
    #word_match_py()
    word_match_sh()

