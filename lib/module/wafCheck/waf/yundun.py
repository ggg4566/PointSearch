#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Yundun Web Application Firewall (Yundun)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"YUNDUN", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= re.search(r"WAF/2\.4-12\.1", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= re.search(r"YUNDUN", headers.get("X-Cache", ""), re.I) is not None
    retval |= "Blocked by YUNDUN Cloud WAF" in (page or "")
    return retval
