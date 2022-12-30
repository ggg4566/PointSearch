#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "DenyALL WAF"


def detect(resp):
    code = resp.status_code
    
    retval = code == 200 and resp.reason == 'Condition Intercepted'
    
    return retval
