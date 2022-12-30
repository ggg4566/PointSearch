#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Reblaze Web Application Firewall (Reblaze)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"\Arbzid=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"Reblaze Secure Web Gateway", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= all(_ in (page or "") for _ in (
    "Current session has been terminated", "For further information, do not hesitate to contact us",
    "Access denied (403)"))
    
    return retval
