#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Bluedon Web Application Firewall (Bluedon Information Security Technology)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"BDWAF", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= re.search(r"Bluedon Web Application Firewall", page or "", re.I) is not None
    
    return retval
