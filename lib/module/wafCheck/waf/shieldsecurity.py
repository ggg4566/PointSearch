#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Shield Security (One Dollar Plugin)"


def detect(resp):
    page = resp.text
    
    retval = "Something in the URL, Form or Cookie data wasn't appropriate" in (page or "")
    
    return retval
