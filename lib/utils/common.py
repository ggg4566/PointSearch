#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/10/23

import os

def list_file(path,filters =[]): #filters =['.txt'...]
    ret = []
    filelist=os.listdir(path)
    for filename in filelist:
        fpath=os.path.join(path,filename)
        if os.path.isdir(fpath):
            list_file(fpath)
        if not os.path.isdir(fpath) and os.path.splitext(fpath)[1] in filters:
            ret.append(fpath)
    return ret

