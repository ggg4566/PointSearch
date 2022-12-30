#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/10/25

import httpx

from lib.core.data import conf,SCAN_RULES
from lib.utils.http import get_ua


def get_arequest_client():
    headers = {'User-Agent': get_ua()}
    transport = httpx.AsyncHTTPTransport(retries=2)
    limit = httpx.Limits(max_connections=None, max_keepalive_connections=None)
    timeout = httpx.Timeout(30,connect=SCAN_RULES['http_timeout'],read=30)
    proxies = {}
    RequestClient = httpx.AsyncClient(transport=transport,limits=limit, verify=False, timeout=timeout, proxies=proxies, headers=headers)
    return RequestClient