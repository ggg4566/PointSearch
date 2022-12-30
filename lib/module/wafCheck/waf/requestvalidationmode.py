#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

__product__ = "ASP.NET RequestValidationMode (Microsoft)"


def detect(resp):
    page = resp.text
    code = resp.status_code
    
    retval = "ASP.NET has detected data in the request that is potentially dangerous" in (page or "")
    retval |= "Request Validation has detected a potentially dangerous client input value" in (page or "")
    retval |= code == 500 and "HttpRequestValidationException" in page
    
    return retval
