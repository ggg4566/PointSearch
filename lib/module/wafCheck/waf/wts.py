#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "WTS Web Application Firewall"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = ">WTS-WAF" in (page or "")
    retval |= re.search(r"\Awts/", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    
    return retval
