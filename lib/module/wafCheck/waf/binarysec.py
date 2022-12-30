#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "BinarySEC Web Application Firewall"


def detect(resp):
    headers = resp.headers

    retval = re.search(r"BinarySec", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= headers.get('x-binarysec-via') is not None
    retval |= headers.get('x-binarysec-nocache') is not None
    return retval
