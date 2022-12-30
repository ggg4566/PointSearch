#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "SiteGuard (JP-Secure)"


def detect(resp):
    page = resp.text
    
    retval = any(_ in (page or "") for _ in ("Powered by SiteGuard", "The server refuse to browse the page"))
    
    return retval
