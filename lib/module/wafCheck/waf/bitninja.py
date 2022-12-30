#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "BitNinja (BitNinja)"


def detect(resp):
    page = resp.text
    
    retval = any(_ in (page or "") for _ in (
        "alt=\"BitNinja|Security check by BitNinja", "your IP will be removed from BitNinja",
        "<title>Visitor anti-robot validation</title>"))
    
    return retval
