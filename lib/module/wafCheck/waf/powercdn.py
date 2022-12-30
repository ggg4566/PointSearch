#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "PowerCDN"


def detect(resp):
    headers = resp.headers

    retval = headers.get("PowerCDN") is not None
    
    return retval
