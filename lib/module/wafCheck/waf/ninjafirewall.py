#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "NinjaFirewall (NinTechNet)"


def detect(resp):
    page = resp.text
    
    retval = "<title>NinjaFirewall: 403 Forbidden" in (page or "")
    retval |= all(_ in (page or "") for _ in ("For security reasons, it was blocked and logged", "NinjaFirewall"))
    
    return retval
