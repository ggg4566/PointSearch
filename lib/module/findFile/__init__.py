#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/7/12

from lib.common.request.connect import WebRequest


def search_file(url,method,timeout):
    code = None
    RequstClient = WebRequest(url,method,timeout)
    RequstClient.connect()
    code = RequstClient.get_response_code()
    return code
