#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/8/22

from lib.core.log import FLY_LOGGER

conf = {'targets':[],
        'action':0,
        'out_file':'',
        'thread_num':2,
        'cookie':'',
        'root_path':"",
        'mode':1
        }

SEARCH_ENG = {'FOFA':{},
              'SHODAN':{}
              }

SCAN_RESULT = {'FOFA_RESULT':[],
               'ZOOMEYE_RESULT':[],
               'RAPID_DNS':[]
               }

SCAN_RULES = {'ports':[],
               'http_code':[],
              'portscan_timeout':5,
              'http_timeout':5,
              'path_deep': 3
               }

DICS_RULES = {'exts':[],
              'year':''
               }

TARGET_DIR_NODE = {'target':"",
               'Path':[]
               }


COLOR ={'red':'\033[1;31;40m',
        'white':'\033[1;37;40m',
        'blue':'\033[1;34;40m',
        'yellow':'\033[1;33;40m',
        'general':'\033[1;32;40m',
        'normal':'\033[0m'}

SCAN_RESULT = {'SCAN_FILE':[],
               'FOFA_RESULT':[],
               'RAPID_DNS':[]
               }

logger = FLY_LOGGER
