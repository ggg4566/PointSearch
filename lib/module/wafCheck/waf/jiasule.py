#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "Jiasule Web Application Firewall (Jiasule)"


def detect(resp):
    page = resp.text
    headers = resp.headers
    code = resp.status_code
    
    retval = re.search(r"jiasule-WAF", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= re.search(r"__jsluid=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"jsl_tracking", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"static\.jiasule\.com/static/js/http_error\.js", page or "", re.I) is not None
    retval |= code == 403 and "notice-jiasule" in (page or "")
    retval |= headers.get('X-Via-JSL') is not None
    
    return retval
