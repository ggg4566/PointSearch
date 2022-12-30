#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/10/22

import string


def get_digits(length):
    ret = []
    digits_list = list(string.digits)
    lens = len(digits_list)
    if (length > lens):
        # logger.error("FuzzDics get_digits param len > 10.")
        return ret
    for i in range(lens):
        v = digits_list[i]
        end_index = i + length
        if (end_index) > lens:
            break
        ret.append("".join(digits_list[i:end_index]))
    return ret

def get_overlap(length):
    ret = []
    digits_list = list(string.digits)
    lens = len(digits_list)
    if (length > lens):
        # logger.error("FuzzDics get_digits param len > 10.")
        return ret
    for i in range(lens):
        v = digits_list[i]*length
        ret.append(v)
    return ret


def get_dics_from_list(l,length): #(['a','b','c'],2) ) => ['ab','bc','cd'....]
    ret = []
    digits_list = l
    lens = len(digits_list)
    if (length > lens):
        # logger.error("FuzzDics get_digits param len > 10.")
        return ret
    for i in range(lens):
        v = digits_list[i]
        end_index = i + length
        if (end_index) > lens:
            break
        ret.append("".join(digits_list[i:end_index]))
    return ret

def get_all_dics_from_list(l,min=2,max=3):
    ret = []
    if min >= max or min < 1:
        return ret
    for i in range(min,max+1):
        v =get_dics_from_list(l,i)
        ret+=v
    return ret


def get_overlap_from_list(l,length):
    ret = []
    digits_list = l
    lens = len(digits_list)
    if (length > lens):
        return ret
    for i in range(lens):
        v = digits_list[i]*length
        ret.append(v)
    return ret

def get_all_overlap_from_list(l,min=1,max=3):
    ret = []
    if min >= max or min < 1:
        return ret
    for i in range(min,max+1):
        v =get_overlap_from_list(l,i)
        ret+=v
    return ret

print(get_digits(3))
l = list("abcde")

print(get_dics_from_list(l,3))
print(get_overlap(3))
print(get_overlap_from_list(l,3))
print(get_all_dics_from_list(l))
print(get_all_overlap_from_list(l))
