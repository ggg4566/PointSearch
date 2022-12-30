#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "CrawlProtect (Jean-Denis Brun)"


def detect(resp):
    page = resp.text
    code = resp.status_code
    
    retval = code >= 400 and "This site is protected by CrawlProtect" in (page or "")
    retval |= "<title>CrawlProtect" in (page or "")
    
    return retval
