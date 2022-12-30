#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/7/9

import requests
import base64
import json
from lib.core.data import SEARCH_ENG,SCAN_RULES,logger
import sys
requests.adapters.DEFAULT_RETRIES = 3  # 增加重连次数
http_timeout = SCAN_RULES['http_timeout']


class sessions(requests.Session):
    def request(self, *args, **kwargs):
        kwargs.setdefault('timeout', http_timeout)
        return super(sessions, self).request(*args, **kwargs)


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
req = sessions()
req.headers = headers
req.keep_alive = False


class Fofa(object):
    def __init__(self,email,api_key):
        self.url = 'https://fofa.so/api/v1/search/all'
        self.req = req
        self.email = email
        self.api_key = api_key
        self.dork  =""
        http_timeout = SCAN_RULES['http_timeout']

    def set_dork(self,dork):
        #v = 'domain={0}'.format(domain)
        search_ = base64.b64encode(str.encode(dork))
        self.dork = search_

    def scan_by_page(self,page,size):
        ret = ''
        params = {'email':self.email,
                  'key':self.api_key,
                  'qbase64':self.dork,
                  'page':page,
                  'size':size
                  }
        try:
            res = self.req.get(self.url,timeout =http_timeout,params = params, headers=headers,verify = False)
            if res.status_code == 200:
                ret = res.text
        except Exception as e:
            logger.error(e)
        return ret

    def scan(self):
        ret = ''
        params = {'email':self.email,
                  'key':self.api_key,
                  'qbase64':self.dork
                  }
        try:
            res = self.req.get(self.url,timeout =http_timeout,params = params, headers=headers,verify = False)
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
                if v['results'] and not v["error"]:
                    data = (v['results'])
            except Exception as e:
                logger.error(e)
        return data

    def get_size(self,html):
        ret = 0
        if html:
            try:
                v = json.loads(html)
                if v['size']:
                    ret=int(v['size'])
            except Exception as e:
                logger.error(e)
        return ret


def fofa_query(domain):
    ret = []
    pepage = 1000
    email = SEARCH_ENG['FOFA']['email']
    api_key = SEARCH_ENG['FOFA']['api_key']
    fofa = Fofa(email,api_key)
    v = 'domain={0}'.format(domain)
    fofa.set_dork(v)
    html = fofa.scan()
    if("401 Unauthorized" in html):
        logger.error(html)
        return ret

    all_total = fofa.get_size(html)
    page_nums = int(all_total/pepage)
    if(all_total>0):
        data =[]
        for i in range(1,page_nums+1):
            _ = fofa.scan_by_page(i,pepage)
            data.extend(fofa.parse_result(_))

        _ = fofa.scan_by_page(page_nums+1,pepage)
        data.extend(fofa.parse_result(_))
        ret = data
    return ret
