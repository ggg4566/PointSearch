#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "NAXSI (NBS System)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"naxsi/waf", headers.get(HTTP_HEADER.X_DATA_ORIGIN, ""), re.I) is not None
    retval |= re.search(r"^naxsi", headers.get(HTTP_HEADER.X_DATA_ORIGIN, ""), re.I) is not None
    retval |= re.search(r"naxsi(.*)?", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= any(_ in (page or "") for _ in ("Blocked By NAXSI", "Naxsi Blocked Information"))
    
    return retval
