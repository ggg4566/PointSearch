#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Cloudbric Web Application Firewall (Cloudbric)"


def detect(resp):
    page = resp.text
    code = resp.status_code
    
    retval = code >= 400 and all(_ in (page or "") for _ in ("Cloudbric", "Malicious Code Detected"))
    
    return retval
