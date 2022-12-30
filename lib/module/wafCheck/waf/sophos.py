#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "UTM Web Protection (Sophos)"


def detect(resp):
    page = resp.text
    
    retval = "Powered by UTM Web Protection" in (page or "")
    
    return retval
