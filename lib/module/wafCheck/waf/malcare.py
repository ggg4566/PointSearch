#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

__product__ = "MalCare (Inactiv.com Media Solutions Pvt Ltd.)"


def detect(resp):
    page = resp.text
    
    retval = "Blocked because of Malicious Activities" in (page or "")
    retval |= re.search(r"Firewall(<[^>]+>)*powered by(<[^>]+>)*MalCare", page or "") is not None
    
    return retval
