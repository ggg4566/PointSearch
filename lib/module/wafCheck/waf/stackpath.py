#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "StackPath Web Application Firewall (StackPath LLC)"


def detect(resp):
    page = resp.text
    
    retval = all(
        _ in (page or "") for _ in ("You performed an action that triggered the service and blocked your request",))
    
    return retval
