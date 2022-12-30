#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import glob
import os
import sys

import requests
from requests import urllib3
from lib.core.data import logger,SCAN_RULES
urllib3.disable_warnings()
from lib.module.wafCheck.config import BASE_DIR, headers, WAF_ATTACK_VECTORS, WAF_KEYWORD_VECTORS, WAF_PRODUCT_NAME

waf_path = BASE_DIR + '/waf/'
sys.path.insert(0, waf_path)
http_timeout = SCAN_RULES['http_timeout']

class WafCheck(object):
    def __init__(self, url):
        
        self.waf_type = ''
        self.info = ''
        self.url = url
        self.waf_list = []
        self.init()
    
    def init(self):
        """
        初始化：加载waf、检查url格式
        """
        for found in glob.glob(os.path.join(waf_path, "*.py")):
            dirname, filename = os.path.split(found)
            if filename == "__init__.py":
                continue
            self.waf_list.append(__import__(filename.split('.')[0]))
        if 'http' not in self.url:
            logger.error('Url format is error. http://www.xxx.com ')

        if not self.url.endswith('/'):
            self.url = self.url + '/'        
    
    def run(self):
        for vector in range(0, len(WAF_ATTACK_VECTORS)):
            payload = WAF_ATTACK_VECTORS[vector]

            payload_url = self.url + payload
            
            try:
                resp = requests.get(payload_url, headers=headers, timeout=http_timeout, allow_redirects=True, verify=False)
            except Exception as e:
                logger.error(e)
                continue
            
            if self.identify_waf(resp):
                logger.success("Found waf: " + self.waf_type)
                return True
            elif resp.status_code != 200:
                self.info = "payload：{}，status_code：{}!!!".format(payload, resp.status_code)
                logger.info("Site Not Found waf or identify fail: " + self.info )
            else:
                self.info = "payload：{}，status_code：{}!!!".format(payload, resp.status_code)
                logger.info("Site Not Found waf or identify fail: " + self.info )
        return False
    
    def check_resp(self, resp):
        content = ''
        if len(resp.text) != 0:
            content = resp.text.strip()
        for waf_keyword in range(0, len(WAF_KEYWORD_VECTORS)):
            if WAF_KEYWORD_VECTORS[waf_keyword] in content:
                self.waf_type = WAF_PRODUCT_NAME[waf_keyword]
                return True
            else:
                self.info = "Site Not Found waf or identify fail!!!"
        return False
    
    def identify_waf(self, resp):
        if not resp.text:
            return
        for waf_mod in self.waf_list:
            if waf_mod.detect(resp):
                self.waf_type = waf_mod.__product__
                return True
            else:
                self.info = "Site Not Found waf or identify fail!!!"
        
        if self.check_resp(resp):
            return True
        return False


def identify_waf(url):
    ret = False
    try:
        wafidentify = WafCheck(url)
        ret = wafidentify.run()
    except Exception as e:
        logger.error("Identify_waf  {0} Exception {1}".format(url,e))
    return ret
