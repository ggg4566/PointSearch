#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Squarespace Web Application Firewall (Squarespace)"


def detect(resp):
    page = resp.text
    
    retval = all(_ in (page or "") for _ in ("BRICK-50", " @ ", "404 Not Found"))
    
    return retval
