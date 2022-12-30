#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Application Security Manager (F5 Networks)"


def detect(resp):
    page = resp.text
    
    retval = "The requested URL was rejected. Please consult with your administrator." in (page or "")
    retval |= all(
        _ in (page or "") for _ in ("security.f5aas.com", "Please enable JavaScript to view the page content"))
    
    return retval
