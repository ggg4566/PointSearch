#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Varnish FireWall (OWASP)"


def detect(resp):
    page = resp.text
    code = resp.status_code

    retval = code >= 400 and "Request rejected by xVarnish-WAF" in (page or "")
    
    return retval
