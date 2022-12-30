#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Tencent Cloud Web Application Firewall (Tencent Cloud Computing)"


def detect(resp):
    page = resp.text
    code = resp.status_code
    
    retval = code == 405 and "waf.tencent-cloud.com" in (page or "")
    
    return retval
