#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "UrlScan (Microsoft)"


def detect(resp):
    page = resp.text
    headers = resp.headers
    code = resp.status_code

    retval = re.search(r"Rejected-By-UrlScan", headers.get(HTTP_HEADER.LOCATION, ""), re.I) is not None
    retval |= code != 200 and re.search(r"/Rejected-By-UrlScan", page or "", re.I) is not None
    retval |= any(_ in (page or "") for _ in ("Rejected-By-UrlScan",
                                              "A custom filter or module, such as URLScan"))
    
    return retval
