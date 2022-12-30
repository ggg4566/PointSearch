#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/7/21
import string
from lib.core.data import DICS_RULES
from lib.common.IPs import is_ip
from lib.core.data import conf
from lib.utils.io import get_file_content,dir_list


class FuzzDics(object):

    def __init__(self, domain):
        self.domain = domain

    def get_dics_from_list(self,l, length):  # (['a','b','c'],2) ) => ['ab','bc','cd'....]
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

    def get_all_dics_from_list(self,l, min=2, max=3):
        ret = []
        if min >= max or min < 1:
            return ret
        for i in range(min, max + 1):
            v = self.get_dics_from_list(l, i)
            ret += v
        return ret

    def get_overlap_from_list(self,l, length):
        ret = []
        digits_list = l
        lens = len(digits_list)
        if (length > lens):
            return ret
        for i in range(lens):
            v = digits_list[i] * length
            ret.append(v)
        return ret

    def get_all_overlap_from_list(self,l, min=1, max=3):
        ret = []
        if min >= max or min < 1:
            return ret
        for i in range(min, max + 1):
            v = self.get_overlap_from_list(l, i)
            ret += v
        return ret
        # 123,234,34
    def get_digits(self,length):
        ret = []
        digits_list = list(string.digits)
        lens = len(digits_list)
        if(length>lens):
            # logger.error("FuzzDics get_digits param len > 10.")
            return ret
        for i in range(lens):
            v = digits_list[i]
            end_index =i +length
            if(end_index)>lens:
                break
            ret.append("".join(digits_list[i:end_index]))
        return ret
        # [11,222,333]
    def get_overlap(self,length):
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
        # keys= ['admin','www',','wwwroot'], exts = ['tar.gz','zip']
    def get_base_keys(self,keys,exts):
        ret = []
        for key in keys:
            for ext in exts:
                v = "{0}.{1}".format(key,ext)
                ret.append(ret)
        return ret

    def get_base_year(self,start_year,end_year):
        ret =[]
        for i in range(start_year,end_year+1):
            ret.append(i)
        return ret

    def get_option_dics(self,keywords,ext):
        ret =[]
        link_char = ['-','_']
        return ret

    def get_domain_dics(self):
        ret = [self.domain]
        if not is_ip(self.domain):
            _ = self.domain.split('.')
            ret+= _[:-1]
        tmp = []
        for i in range(1, 4):
            t = FuzzDics("")
            tmp += t.get_digits(i)
        length = len(ret)
        m = ret
        for i in range(length):
            d =ret[i]
            for v in tmp:
                m.append(d+v)
        return m


def get_base_keys(domain):
    ret =[]
    t = FuzzDics(domain)
    for i in range(1,5):
        ret+=t.get_digits(i)
    for i in range(2,5):
        ret+=t.get_overlap(i)
    start_year,end_year = DICS_RULES['year'].split('-')
    ret +=t.get_base_year(int(start_year),int(end_year))
    ret +=t.get_domain_dics()
    chars = list("abcde")
    ret +=t.get_all_dics_from_list(chars)
    ret +=t.get_all_overlap_from_list(chars)
    return ret


def get_custom_file_dics(domain):
    custom_dics = []
    base_keys =get_base_keys(domain)
    file_name =get_filename_dics()
    base_keys+= file_name
    file_exts = DICS_RULES['exts']
    for k in base_keys:
        for ext in file_exts:
            var = "{0}.{1}".format(k,ext)
            custom_dics.append(var)
    custom_dics+= get_file_dics()
    ret = list(set(custom_dics))
    return ret


def get_path_dics(paths):
    ret = []
    for path in paths:
        #ret.append(path)
        if '/' in path:
            l = path.split('/')
            key = l[-1]
            tmp = []
            tmp = get_custom_file_dics(key)
            ret += [path+'/'+ v for v in tmp]
            _= path.split('/')
            last_path = "/".join(_[:-1])
            if last_path:
                ret += [last_path + '/' + v for v in tmp]
            else:
                ret += ['/' + v for v in tmp]
        else:
            tmp = []
            tmp = get_custom_file_dics(path)
            ret += [path + '/' + v for v in tmp]
    return ret


def get_dir_dics():
    ret = []
    dir_path = conf['root_path'] +'/dics/dirs'
    filters = ['.txt']
    files =dir_list(dir_path,filters)
    for file in files:
        _= get_file_content(file)
        ret += _
    return ret


def get_file_dics():
    ret = []
    dir_path = conf['root_path'] +'/dics/file'
    filters = ['.txt']
    files =dir_list(dir_path,filters)
    for file in files:
        _= get_file_content(file)
        ret += _
    return ret


def get_sensive_dics():
    ret = []
    dir_path = conf['root_path'] +'/dics/sensive'
    filters = ['.txt']
    files =dir_list(dir_path,filters)
    for file in files:
        _= get_file_content(file)
        ret += _
    return ret


def get_filename_dics():
    ret = []
    dir_path = conf['root_path'] +'/dics/filenames'
    filters = ['.txt']
    files =dir_list(dir_path,filters)
    for file in files:
        _= get_file_content(file)
        ret += _
    return ret

