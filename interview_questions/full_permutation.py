#!/usr/bin/env python3
#
# Interview question of DiDi.com: FuLL Permutation

__author__ = 'zifengw'

def full_permutation(dict):
    L_values = []
    for key in dict.keys():
        L_values.append(dict[key])

    L_tmp = [L_v1 + ' ' + L_v2 + ' ' + L_v3 \
            for L_v1 in L_values[0] \
            for L_v2 in L_values[1] \
            for L_v3 in L_values[2]]
    
    return L_tmp

if __name__ == '__main__':
    dict = {'City': ['Beijing', 'Shanghai', 'Tianjin', 'Hangzhou'], 
            'Cars': ['BMW', 'Audi'], 
            'Color': ['Red', 'BLue', 'Yellow']}

    L_full = full_permutation(dict)
    for tmp in L_full:
        print('%s' % tmp)

