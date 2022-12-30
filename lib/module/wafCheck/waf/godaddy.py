#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "GoDaddy Website Firewall (GoDaddy Inc.)"


def detect(resp):
    page = resp.text
    
    retval = any(_ in (page or "") for _ in
                 ("Access Denied - GoDaddy Website Firewall", "<title>GoDaddy Security - Access Denied</title>"))
    
    return retval
