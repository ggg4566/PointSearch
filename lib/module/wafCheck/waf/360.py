#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""
import re

__product__ = "360 Web Application Firewall (360)"


def detect(resp):
    page = resp.text
    headers = resp.headers
    code = resp.status_code
    retval = headers.get("X-Powered-By-360wzb") is not None
    retval |= headers.get("x-powered-by-360wzb") is not None
    retval |= re.search(r"wangzhan\.360\.cn", headers.get("x-powered-by-360wzb", ""), re.I) is not None
    retval |= code == 493 and "/wzws-waf-cgi/" in (page or "")
    retval |= all(_ in (page or "") for _ in ("eventID", "If you are the Webmaster", "<title>493</title>"))
    retval |= "360websec notice:Illegal operation!" in page
    
    return retval
