#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "dotDefender (Applicure Technologies)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = headers.get("X-dotDefender-denied", "") == "1"
    retval |= headers.get("X-dotDefender-denied") is not None
    retval |= any(_ in (page or "") for _ in ("dotDefender Blocked Your Request",
                                              '<meta name="description" content="Applicure is the leading provider of web application security',
                                              "Please contact the site administrator, and provide the following Reference ID:"))
    
    return retval
