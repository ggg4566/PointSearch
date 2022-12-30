#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Safedog Web Application Firewall (Safedog)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"WAF/2\.0", headers.get(HTTP_HEADER.X_POWERED_BY, ""), re.I) is not None
    retval |= re.search(r"Safedog", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= re.search(r"safedog", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"^safedog-flow-item=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= any(_ in (page or "") for _ in ("safedogsite/broswer_logo.jpg", "404.safedog.cn/sitedog_stat.html",
                                              "404.safedog.cn/images/safedogsite/head.png"))
    
    return retval
