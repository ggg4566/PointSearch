#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Armor Protection (Armor Defense)"


def detect(resp):
    page = resp.text
    
    retval = "This request has been blocked by website protection from Armor" in (page or "")
    
    return retval
