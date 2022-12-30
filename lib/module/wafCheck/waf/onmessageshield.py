#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

__product__ = "onMessage Shield (Blackbaud)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"onMessage Shield", headers.get("X-Engine", ""), re.I) is not None
    retval |= "This site is protected by an enhanced security system to ensure a safe browsing experience" in (
                page or "")
    retval |= "onMessage SHIELD" in (page or "")
    
    return retval
