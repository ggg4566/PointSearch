#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "PerimeterX (PerimeterX, Inc.)"


def detect(resp):
    page = resp.text
    
    retval = "https://www.perimeterx.com/whywasiblocked" in (page or "")
    
    return retval
