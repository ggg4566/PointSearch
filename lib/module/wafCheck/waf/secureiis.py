#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

__product__ = "SecureIIS Web Server Security (BeyondTrust)"


def detect(resp):
    page = resp.text
    
    retval = re.search(r"SecureIIS[^<]+Web Server Protection", page or "") is not None
    retval |= "http://www.eeye.com/SecureIIS/" in (page or "")
    retval |= re.search(r"\?subject=[^>]*SecureIIS Error", page or "") is not None
    retval |= any(_ in (page or "") for _ in ("SecureIIS is an internet security application",
                                              "Download SecureIIS Personal Edition",
                                              "http://www.eeye.com/SecureIIS/"))
    
    return retval
