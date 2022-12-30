#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "aeSecure (aeSecure)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = headers.get("aeSecure-code") is not None
    retval |= all(_ in (page or "") for _ in ("aeSecure", "aesecure_denied.png"))
    
    return retval
