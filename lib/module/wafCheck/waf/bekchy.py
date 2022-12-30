#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Bekchy (Faydata Information Technologies Inc.)"


def detect(resp):
    page = resp.text
    
    retval = any(_ in (page or "") for _ in
                 ("<title>Bekchy - Access Denided</title>", "<a class=\"btn\" href=\"https://bekchy.com/report\">"))
    
    return retval
