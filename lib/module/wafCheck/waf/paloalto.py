#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

__product__ = "Palo Alto Firewall (Palo Alto Networks)"


def detect(resp):
    page = resp.text
    
    retval = re.search(r"has been blocked in accordance with company policy", page or "", re.I) is not None
    retval |= all(_ in (page or "") for _ in ("Palo Alto Next Generation Security Platform", "Download Blocked"))
    
    return retval
