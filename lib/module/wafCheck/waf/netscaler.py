#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""
import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "NetScaler AppFirewall (Citrix)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"\A(ns_af=|citrix_ns_id|NSC_)", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r"^(ns_af=|citrix_ns_id|NSC_)", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r"\/vpn\/index\.html", headers.get(HTTP_HEADER.LOCATION, ""), re.I) is not None
    
    retval |= re.search(r"NS-CACHE", headers.get("Via", ""), re.I) is not None
    
    retval |= headers.get("Cneonction") is not None
    
    retval |= headers.get("nnCoection") is not None
    
    retval |= any(_ in (page or "") for _ in (
        "<title>Application Firewall Block Page</title>", "Violation Category: APPFW_", "AppFW Session ID",
        "Access has been blocked - if you feel this is in error, please contact the site administrators quoting the following",
        "NS Transaction ID:", "Citrix|NetScaler"))
    
    return retval
