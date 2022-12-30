#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "SiteGround Web Application Firewall (SiteGround)"


def detect(resp):
    page = resp.text
    
    retval = "The page you are trying to access is restricted due to a security rule" in (page or "")
    
    return retval
