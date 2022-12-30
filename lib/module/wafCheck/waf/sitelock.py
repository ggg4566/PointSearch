#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
# Note: https://www.whitefirdesign.com/blog/2016/11/08/more-evidence-that-sitelocks-trueshield-web-application-firewall-is-really-incapsulas-waf/
"""

__product__ = "TrueShield Web Application Firewall (SiteLock)"


def detect(resp):
    page = resp.text
    
    retval = any(_ in (page or "") for _ in ("SiteLock Incident ID", '<span class="value INCIDENT_ID">'))
    
    return retval
