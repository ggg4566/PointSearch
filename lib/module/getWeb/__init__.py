#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/7/9
from lib.common.request.connect import WebRequest
from lib.core.enums import REQUEST_METHOD
from lib.core.data import  SCAN_RULES

def init_scan_url(targets):
    ret = []
    for target in targets:
        host = target['host']
        port = target['port']
        if (port == 443):
            url = 'https://{0}'.format(host)
            ret.append(url)
        elif (port == 80):
            url = 'http://{0}'.format(host)
            ret.append(url)
        else:
            url = 'http://{0}:{1}'.format(host,port)
            ret.append(url)
            url = 'https://{0}:{1}'.format(host,port)
            ret.append(url)
    return ret


def find_web(url):
    code = None
    RequstClient = WebRequest(url,REQUEST_METHOD.HEAD , SCAN_RULES['http_timeout'])
    RequstClient.connect()
    code = RequstClient.get_response_code()
    return code