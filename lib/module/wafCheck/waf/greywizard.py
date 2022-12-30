#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Greywizard (Grey Wizard)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"\Agreywizard", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= any(_ in (page or "") for _ in (
    "We've detected attempted attack or non standard traffic from your IP address", "<title>Grey Wizard</title>"))
    
    return retval
