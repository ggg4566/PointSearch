#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/8/22
import os


def put_file_contents(filename,contents):
    with open(filename,"a+") as fin:
        fin.write(contents+'\n')


def read_file_con(filename):
    contents=""
    with open(filename,"r") as fin:
        contents=fin.read()
    return contents


def get_file_content(filename):
    result = []
    f = open(filename, "r")
    for line in f.readlines():
        if line:
            result.append(line.strip())
    f.close()
    return result


def dir_list(path,filters):
    list =[]
    filelist=os.listdir(path)
    for filename in filelist:
        fpath=os.path.join(path,filename)
        if os.path.isdir(fpath):
            dir_list(fpath,filters)
        if not os.path.isdir(fpath) and os.path.splitext(fpath)[1] in filters:
            list.append(fpath)
    return list