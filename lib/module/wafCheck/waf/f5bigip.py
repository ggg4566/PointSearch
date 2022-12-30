#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "F5 Networks BIG-IP Application Security Manager"


def detect(resp):
    headers = resp.headers

    retval = re.search(r"BigIP", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    
    retval |= re.search(r"^TS[a-zA-Z0-9]{3,8}=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r"^BIGipServer", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r"BIGipServer", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    
    retval |= re.search(r"^close$", headers.get("X-Cnection", ""), re.I) is not None
    
    retval |= re.search(r"BigIP|BIG-IP|BIGIP", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    
    retval |= re.search(r"BigIP|BIG-IP|BIGIP", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None \
              and re.search(r"^MRHSession", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"^LastMRH_Sessio", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None \
              and re.search(r"^MRHSession", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r'\/my\.policy', headers.get(HTTP_HEADER.LOCATION, ""), re.I) is not None \
              and re.search(r"BigIP|BIG-IP|BIGIP", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= re.search(r'\/my\.logout\.php3', headers.get(HTTP_HEADER.LOCATION, ""), re.I) is not None \
              and re.search(r"BigIP|BIG-IP|BIGIP", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= re.search(r'.+\/f5\-w\-68747470.+', headers.get(HTTP_HEADER.LOCATION, ""), re.I) is not None \
              and re.search(r"BigIP|BIG-IP|BIGIP", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    
    retval |= re.search(r"^F5_fullWT", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None \
              or re.search(r"^F5_ST", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None \
              or re.search(r"^F5_HT_shrinked", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r"^MRHSequence", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None \
              or re.search(r"^MRHSHint", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None \
              or re.search(r"^LastMRH_Session", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r'\/my\.logon\.php3', headers.get(HTTP_HEADER.LOCATION, ""), re.I) is not None \
              and re.search(r"^VHOST", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r'^MRHSession', headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None \
              and re.search(r"^VHOST", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None \
              or re.search(r"^uRoamTestCookie", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r'^MRHSession', headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None \
              and re.search(r"^MRHCId", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None \
              or re.search(r"^MRHIntranetSession", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r'^uRoamTestCookie', headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None \
              or re.search(r"^VHOST", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r'^ASINFO=', headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    retval |= re.search(r'F5-TrafficShield', headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None

    return retval
