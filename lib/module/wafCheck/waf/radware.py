#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

__product__ = "AppWall (Radware)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"Unauthorized Activity Has Been Detected.+Case Number:", page or "", re.I | re.S) is not None
    retval |= headers.get("X-SL-CompState") is not None
    retval |= "CloudWebSec@radware.com" in (page or "")
    retval |= any(_ in (page or "") for _ in (
        "because we have detected unauthorized activity", "<TITLE>Unauthorized Request Blocked</TITLE>",
        "If you believe that there has been some mistake", "?Subject=Security Page - Case Number"))
    
    return retval
