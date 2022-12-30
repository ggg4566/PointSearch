#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Distil Web Application Firewall Security (Distil Networks)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = headers.get("x-distil-cs") is not None
    retval |= any(_ in (page or "") for _ in
                  ("distilCaptchaForm", "distilCallbackGuard", "cdn.distilnetworks.com/images/anomaly-detected.png"))
    
    return retval
