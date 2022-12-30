#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""
import re

__product__ = "ChinaCache (ChinaCache Networks)"


def detect(resp):
    headers = resp.headers
    code = resp.status_code
    
    retval = code >= 400 and headers.get("Powered-By-ChinaCache") is not None
    retval |= re.search(r".+", headers.get("Powered-By-ChinaCache", ""), re.I) is not None
    
    return retval
