#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/7/9

import requests
import base64
import json
import sys
import time
from lib.core.data import SCAN_RULES,SEARCH_ENG,conf,logger

requests.adapters.DEFAULT_RETRIES = 3  # 增加重连次数
http_timeout = SCAN_RULES['http_timeout']


class sessions(requests.Session):
    def request(self, *args, **kwargs):
        kwargs.setdefault('timeout', http_timeout)
        return super(sessions, self).request(*args, **kwargs)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
#req = requests.session()
req = sessions()
req.headers = headers
req.keep_alive = False

#req.proxies = {"http":"127.0.0.1:8080","https":"127.0.0.1:8080"}


class RapidDns(object):
    def __init__(self):
        self.url = 'https://rapiddns.io/api/v1/'
        http_timeout = SCAN_RULES['http_timeout']
    def scan_by_page(self,domain,page,size):
        ret = ''
        params = {
                  'page':page,
                  'size':size
                  }
        try:
            #time.sleep(2)
            res = req.get(self.url+domain,timeout =http_timeout,params = params, headers=headers,verify = False)
            if res.status_code == 200:
                ret = res.text
        except Exception as e:
            logger.error(e)
        return ret

    def scan(self,domain):
        ret = ''
        try:
            res = req.get(self.url+domain,timeout =http_timeout, headers=headers,verify = False)
            if res.status_code == 200:
                ret = res.text
        except Exception as e:
            logger.error(e)
        return ret

    def parse_result(self,html):
        data = []
        if html:
            try:
                v = json.loads(html)
                if v['data']:
                    data = (v['data'])
            except Exception as e:
                logger.error(e)
        return data

    def get_size(self,html):
        ret = 0
        if html:
            try:
                v = json.loads(html)
                if v['total']:
                    ret=int(v['total'])
            except Exception as e:
                logger.error(e)
        return ret


def rapid_query(domain):
    ret = []
    pepage = 1000

    Rapid = RapidDns()
    html = Rapid.scan_by_page(domain,1,1)

    all_total = Rapid.get_size(html)
    page_nums= int(all_total/pepage)+1
    if(all_total>0):
        data =[]
        for i in range(1,page_nums+1):
            _ = Rapid.scan_by_page(domain,i,pepage)
            data.extend(Rapid.parse_result(_))
            logger.info("All Entry:%s/%s page,Current page:%s"%(all_total,page_nums,i))
        _ = Rapid.scan_by_page(domain,page_nums+1,pepage)
        data.extend(Rapid.parse_result(_))
        ret = data
    return ret
