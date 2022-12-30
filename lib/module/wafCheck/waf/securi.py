#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Sucuri WebSite Firewall"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"Sucuri/Cloudproxy", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= headers.get("X-Sucuri-ID") is not None
    retval |= headers.get("X-Sucuri-Cache") is not None
    retval |= headers.get("X-Sucuri-Block") is not None
    retval |= any(_ in (page or "") for _ in ("Access Denied - Sucuri Website Firewall",
                                              "<title>Sucuri WebSite Firewall - Access Denied</title>",
                                              "https://sucuri.net/privacy-policy",
                                              "https://cdn.sucuri.net/sucuri-firewall-block.css",
                                              "Sucuri Inc.",
                                              "cloudproxy@sucuri.net"))
    
    return retval
