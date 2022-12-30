#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "ExpressionEngine (EllisLab)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = any((page or "").strip() == _ for _ in ("Invalid GET Data", "Invalid URI")) and re.search(r"\bexp_last_",
                                                                                                       headers.get(
                                                                                                           HTTP_HEADER.SET_COOKIE,
                                                                                                           ""),
                                                                                                       re.I) is not None
    
    return retval
