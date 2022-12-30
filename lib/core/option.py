#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/8/22

from lib.core.data import conf
from lib.parse.parse import parse_cmd_line
from lib.utils.io import get_file_content
from lib.core.common import set_search_engine
from lib.utils.proxy import set_proxy
import sys


def init_options():
    commond_lines = parse_cmd_line()
    hosts = []
    if commond_lines.proxy:
        set_proxy(commond_lines.proxy)
    if commond_lines.domain:
        hosts = [commond_lines.domain]
    else:
        hosts =get_file_content(commond_lines.file)
    conf['thread_num'] = commond_lines.thread_num
    conf['targets'] = hosts
    conf['action'] =commond_lines.action
    conf['out_file'] = commond_lines.out
    conf['mode'] = commond_lines.mode
    set_search_engine()
    return