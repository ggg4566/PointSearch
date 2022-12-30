#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Safe3 Web Application Firewall"


def detect(resp):
    headers = resp.headers

    retval = headers.get('X-DIS-Request-ID') is not None
    retval |= re.search(r"DOSarrest", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    
    return retval
