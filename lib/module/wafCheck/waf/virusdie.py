#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "Virusdie (Virusdie LLC)"


def detect(resp):
    page = resp.text
    
    retval = any(_ in (page or "") for _ in (
    "| Virusdie</title>", "http://cdn.virusdie.ru/splash/firewallstop.png", "&copy; Virusdie.ru</p>",
    '<meta name="FW_BLOCK"'))
    
    return retval
