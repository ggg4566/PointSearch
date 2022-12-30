#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "CloudProxy WebSite Firewall (Sucuri)"


def detect(resp):
    page = resp.text
    headers = resp.headers
    code = resp.status_code
    
    retval = code == 403 and re.search(r"Sucuri/Cloudproxy", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= "Access Denied - Sucuri Website Firewall" in (page or "")
    retval |= "Sucuri WebSite Firewall - CloudProxy - Access Denied" in (page or "")
    retval |= re.search(r"Questions\?.+cloudproxy@sucuri\.net", (page or "")) is not None
    retval |= headers.get("X-Sucuri-ID") is not None
    retval |= headers.get("X-Sucuri-Cache") is not None
    
    return retval
