#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Incapsula Web Application Firewall (Incapsula/Imperva)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"incap_ses|visid_incap", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"Incapsula", headers.get("X-CDN", ""), re.I) is not None
    retval |= re.search(r"^incap_ses.*=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"^visid_incap.*=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= "Incapsula incident ID" in (page or "")
    retval |= all(_ in (page or "") for _ in ("Error code 15", "This request was blocked by the security rules"))
    retval |= all(_ in (page or "") for _ in ("Incapsula incident ID:", "/_Incapsula_Resource"))
    retval |= re.search(r"(?i)incident.{1,100}?\b\d{19}\-\d{17}\b", page or "") is not None
    retval |= headers.get("X-Iinfo") is not None
    
    return retval
