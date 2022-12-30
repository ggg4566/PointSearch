#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Microsoft ISA Server"


def detect(resp):
    page = resp.text
    
    isaservermatch = [
        'Forbidden ( The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.  )',
        'Forbidden ( The ISA Server denied the specified Uniform Resource Locator (URL)'
    ]
    retval = resp.reason in isaservermatch
    
    retval |= all(_ in (page or "") for _ in ("The ISA Server denied the specified Uniform Resource Locator (URL)",
                                              "The server denied the specified Uniform Resource Locator (URL). Contact the server administrator."))

    return retval
