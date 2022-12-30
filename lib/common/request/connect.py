#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/7/9
import requests
import random
from lib.core.enums import REQUEST_METHOD
from lib.core.data import logger
requests.adapters.DEFAULT_RETRIES = 3  # 增加重连次数


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}
req = requests.session()
req.headers = headers
req.keep_alive = False

# Disable SSL warnings
try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()

except Exception:
    pass


class WebRequest(object):
    def __init__(self,url,method,timeout):
        self.url = url
        self.method = method
        self.timeout = timeout
        self.staus_code = None
        self.text = ""
        self.header = {'User-Agent': self.get_ua(), 'Accept': '*/*'}

    def set_options(self,url,method,timeout):
        self.url = url
        self.method = method
        self.timeout = timeout

    def get_ua(self):
        agents = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) " +
            "Gecko/20100101 Firefox/51.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0)" +
            " Gecko/20100101 Firefox/51.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
            "AppleWebKit/537.36 (KHTML, like Gecko) " +
            "Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
            "AppleWebKit/537.36 (KHTML, like Gecko) " +
            "Chrome/56.0.2924.87 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; " +
            "Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Macintosh; Intel Mac OS " +
            "X 10_12_2) AppleWebKit/602.3.12 (KHTML, " +
            "like Gecko) Version/10.0.2 Safari/602.3.12",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; " +
            "rv:51.0) Gecko/20100101 Firefox/51.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 " +
            "like Mac OS X) AppleWebKit/602.4.6 (KHTML, " +
            "like Gecko) Version/10.0 Mobile/14D27" +
            " Safari/602.1",
            "Mozilla/5.0 (Linux; Android 6.0.1; " +
            "Nexus 6P Build/MTC19X) AppleWebKit/537.36 " +
            "(KHTML, like Gecko) Chrome/56.0.2924.87 " +
            "Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 " +
            "Build/KTU84P) AppleWebKit/537.36 (KHTML, " +
            "like Gecko) Chrome/56.0.2924.87" +
            "Mobile Safari/537.36",
            "Mozilla/5.0 (compatible; Googlebot/2.1; " +
            "+http://www.google.com/)"
        ]
        return random.choice(agents)

    def connect(self):
        try:
            if(self.method == REQUEST_METHOD.GET):
                req.headers = self.header
                res =req.get(self.url,timeout =self.timeout,verify=False)
                self.staus_code = res.status_code
                self.text = res.text

            elif(self.method == REQUEST_METHOD.POST):
                req.headers = self.header
                res =req.post(self.url,timeout =self.timeout,verify=False)
                self.staus_code = res.status_code
                self.text = res.text
            else:
                req.headers = self.header
                res = req.head(self.url,timeout =self.timeout,verify=False)
                self.staus_code = res.status_code
        except Exception as e:
            logger.error(e)

    def get_response_text(self):
        return self.text

    def get_response_code(self):
        return self.staus_code

