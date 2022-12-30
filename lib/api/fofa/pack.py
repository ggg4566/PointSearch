#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/8/22
import requests
import base64
import json
from lib.core.data import SEARCH_ENG,conf
requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
req = requests.session()
req.headers = headers


class Fofa(object):
    def __init__(self,email,api_key):
        self.url = 'https://classic.fofa.so/api/v1/search/all'
        self.req = req
        self.email = email
        self.api_key = api_key

    def scan(self,ip):

        ret = ''
        url = self.url
        if conf['www_scan']:
            v = 'ip={0}&&type=subdomain'.format(ip)
            search_ = base64.b64encode(str.encode(v))
            params = {'email':self.email,
                      'key':self.api_key,
                      'qbase64':search_,
                      'fields': 'host,title'
                      }
        else:
            v = 'ip={0}'.format(ip)
            search_ = base64.b64encode(str.encode(v))
            params = {'email':self.email,
                      'key':self.api_key,
                      'qbase64':search_,
                      'fields':'port'
                      }
        try:
            res = self.req.get(url,params = params, headers=headers,verify = False)
            if res.status_code == 200:
                ret = res.content
        except Exception as e:
            print(e)
        return ret

    def parse_result(self,html):
        data = []
        if html:
            try:
                v = json.loads(html)
                if v['results'] and not v["error"]:
                    data = (v['results'])
            except Exception as e:
                print(e)
        return data


def fofa_query(host):
    ret = []
    email = SEARCH_ENG['FOFA']['email']
    api_key = SEARCH_ENG['FOFA']['api_key']
    fofa = Fofa(email,api_key)
    html = fofa.scan(host)
    ret = fofa.parse_result(html)
    return ret

