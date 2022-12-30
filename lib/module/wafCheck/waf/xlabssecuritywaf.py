#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""
import re

__product__ = "XLabs Security WAF"


def detect(resp):
    headers = resp.headers

    retval = re.search(r"XLabs Security", headers.get("x-cdn", ""), re.I) is not None
    retval |= re.search(r"XLabs WAF(.*)?", headers.get("server", ""), re.I) is not None
    
    return retval
