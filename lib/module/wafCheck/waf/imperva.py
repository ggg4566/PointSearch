#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

__product__ = "Imperva SecureSphere"


def detect(resp):
    page = resp.text
    
    retval = all(_ in (page or "") for _ in ("<H2>Error</H2>", "<title>Error</title>", "The incident ID is:",
                                             "This page can't be displayed.",
                                             "Contact support for additional information."))
    
    return retval
