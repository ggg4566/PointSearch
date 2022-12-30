#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/8/22

from lib.core.data import SEARCH_ENG
import shodan
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}


class Shodan(object):
    def __init__(self,api_key):
        self.api_key = api_key

    def scan(self,ip):
        ret = []
        try:
            api = shodan.Shodan(self.api_key)
            hx = api.host('{}'.format(ip))
            for item in hx['data']:
                port = str(item['port'])
                ret.append(port)
        except shodan.APIError as e:
            print('[-]Error:', e)
        return ret

def shodan_query(host):
    ret = []
    api_key = SEARCH_ENG['SHODAN']['api_key']
    shodan = Shodan(api_key)
    ret= shodan.scan(host)
    return ret

