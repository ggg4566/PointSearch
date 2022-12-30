#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "WebKnight Application Firewall (AQTRONIX)"


def detect(resp):
    page = resp.text
    headers = resp.headers
    code = resp.status_code

    retval = code == 999
    retval |= code == 999 and resp.reason == 'No Hacking'
    retval |= code == 404 and resp.reason == 'Hack Not Found'
    
    retval |= re.search(r"WebKnight", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= any(_ in (page or "") for _ in ("WebKnight Application Firewall Alert", "AQTRONIX WebKnight",
                                              "What is WebKnight?",
                                              "WebKnight will take over and protect",
                                              "http://www.aqtronix.com/WebKnight"))
    
    return retval
