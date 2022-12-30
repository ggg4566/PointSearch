#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

__product__ = "SecureSphere Web Application Firewall (Imperva)"


def detect(resp):
    page = resp.text
    
    retval = re.search(
        r"<H2>Error</H2>.+?#FEEE7A.+?<STRONG>Error</STRONG>|Contact support for additional information.<br/>The incident ID is: (\\d{19}|N/A)",
        page or "", re.I) is not None
    
    return retval
