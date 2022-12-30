#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "RSFirewall (RSJoomla!)"


def detect(resp):
    page = resp.text
    
    retval = any(_ in (page or "") for _ in ("COM_RSFIREWALL_403_FORBIDDEN", "COM_RSFIREWALL_EVENT"))
    
    return retval
