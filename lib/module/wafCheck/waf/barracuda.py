#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Barracuda Web Application Firewall (Barracuda Networks)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"\Abarra_counter_session=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"^barra_counter_session=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"^BNI__BARRACUDA_LB_COOKIE=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"^BNI_persistence=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"^BN[IE]S_.*?=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"(\A|\b)barracuda_", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"Barracuda", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= "when this page occurred and the event ID found at the bottom of the page" in (page or "")
    retval |= "Barracuda Networks, Inc" in (page or "")
    
    return retval
