#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "FortiWeb Web Application Firewall (Fortinet)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"\AFORTIWAFSID=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"FORTIWAFSID=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= all(_ in (page or "") for _ in (".fgd_icon", ".blocked", ".authenticate", "Web Page Blocked", "URL:",
                                              "Attack ID", "Message ID", "Client IP"))
    
    return retval
