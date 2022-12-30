#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/10/21

from tqdm import tqdm

bar=""

def create_bar(l):
    global bar
    bar = tqdm(l,ncols=100)

def print_progress(v):
    bar.update(1)




