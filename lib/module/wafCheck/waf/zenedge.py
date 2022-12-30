#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Zenedge Web Application Firewall (Zenedge)"


def detect(resp):
    page = resp.text
    headers = resp.headers
    code = resp.status_code

    retval = code >= 400 and re.search(r"\AZENEDGE", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= all(_ in (page or "") for _ in ("Your request has been blocked", "Incident ID", "/__zenedge/assets/"))
    
    return retval
