#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""
import re

__product__ = "Anquanbao Web Application Firewall (Anquanbao)"


def detect(resp):
    page = resp.text
    headers = resp.headers
    code = resp.status_code
    
    retval = code == 405 and any(_ in (page or "") for _ in ("/aqb_cc/error/", "hidden_intercept_time"))
    retval |= headers.get("X-Powered-By-Anquanbao") is not None
    retval |= re.search(r"MISS", headers.get("X-Powered-By-Anquanbao", ""), re.I) is not None
    
    return retval
