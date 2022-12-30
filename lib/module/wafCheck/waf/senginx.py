#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "SEnginx (Neusoft Corporation)"


def detect(resp):
    page = resp.text
    
    retval = "SENGINX-ROBOT-MITIGATION" in (page or "")
    
    return retval
