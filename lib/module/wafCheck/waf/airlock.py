#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Airlock (Phion/Ergon)"


def detect(resp):
    page = resp.text
    headers = resp.headers
    retval = re.search(r"\AAL[_-]?(SESS|LB)", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"^AL[_-]?(SESS|LB)=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= all(_ in (page or "") for _ in (
        "The server detected a syntax error in your request", "Check your request and all parameters", "Bad Request",
        "Your request ID was"))
    
    return retval
