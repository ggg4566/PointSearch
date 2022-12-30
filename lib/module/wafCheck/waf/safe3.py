#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Safe3 Web Application Firewall"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"Safe3WAF", headers.get(HTTP_HEADER.X_POWERED_BY, ""), re.I) is not None
    retval |= re.search(r"Safe3 Web Firewall", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= all(_ in (page or "") for _ in ("403 Forbidden", "Safe3waf/"))
    
    return retval
