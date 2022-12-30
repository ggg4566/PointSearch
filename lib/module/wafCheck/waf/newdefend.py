#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Newdefend Web Application Firewall (Newdefend)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"NewDefend", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= any(_ in (page or "") for _ in ("/nd_block/", "http://www.newdefend.com/feedback/misinformation/"))
    
    return retval
