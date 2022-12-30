#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "SafeLine Next Gen WAF (Chaitin Tech)"


def detect(resp):
    page = resp.text
    
    retval = all(_ in (page or "") for _ in ("SafeLine", "<!-- event_id:"))
    
    return retval
