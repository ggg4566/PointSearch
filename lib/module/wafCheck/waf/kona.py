#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "KONA Security Solutions (Akamai Technologies)"


def detect(resp):
    headers = resp.headers
    code = resp.status_code
    
    retval = code >= 400 and re.search(r"AkamaiGHost", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    
    return retval
