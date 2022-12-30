#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Janusec Application Gateway (Janusec)"


def detect(resp):
    page = resp.text
    
    retval = all(_ in (page or "") for _ in ("Reason:", "by Janusec Application Gateway"))
    
    return retval
