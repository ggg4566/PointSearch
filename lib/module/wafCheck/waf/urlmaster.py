#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Url Master SecurityCheck (iFinity/DotNetNuke)"


def detect(resp):
    page = resp.text
    code = resp.status_code

    retval = code >= 400 and all(_ in (page or "") for _ in ("UrlMaster", "UrlRewriteModule", "SecurityCheck"))
    
    return retval
