#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Mission Control Application Shield"


def detect(resp):
    headers = resp.headers

    retval = re.search(r"Mission Control Application Shield", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    
    return retval
