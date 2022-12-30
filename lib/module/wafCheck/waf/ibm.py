#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

__product__ = "IBM WebSphere DataPower"


def detect(resp):
    headers = resp.headers

    # retval = headers.get('X-Backside-Transport') is not None
    retval = re.search(r"\A(OK|FAIL)", headers.get("X-Backside-Transport", ""), re.I) is not None
    retval |= re.search(r"^(OK|FAIL)", headers.get("X-Backside-Transport", ""), re.I) is not None
    return retval
