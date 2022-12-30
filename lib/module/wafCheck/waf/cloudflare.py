#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.module.wafCheck.config import HTTP_HEADER

__product__ = "CloudFlare Web Application Firewall (CloudFlare)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = False

    retval |= re.search(r"cloudflare", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= re.search(r"\A__cfduid=", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= re.search(r"__cfduid", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    retval |= headers.get("cf-ray") is not None
    retval |= re.search(r"CloudFlare Ray ID:|var CloudFlare=", page or "") is not None
    retval |= all(_ in (page or "") for _ in
                  ("Attention Required! | Cloudflare", "Please complete the security check to access"))
    retval |= all(_ in (page or "") for _ in ("Attention Required! | Cloudflare", "Sorry, you have been blocked"))
    retval |= any(_ in (page or "") for _ in ("CLOUDFLARE_ERROR_500S_BOX", "::CAPTCHA_BOX::"))

    return retval
