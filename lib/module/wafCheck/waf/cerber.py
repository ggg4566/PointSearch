#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "WP Cerber Security (Cerber Tech)"


def detect(resp):
    page = resp.text
    
    retval = any(_ in (page or "") for _ in ("We're sorry, you are not allowed to proceed",
                                             "Your request looks suspicious or similar to automated requests from spam posting software"))
    
    return retval
