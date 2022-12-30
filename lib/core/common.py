#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/9/9

from lib.core.data import conf,SEARCH_ENG,SCAN_RULES,DICS_RULES
from lib.utils.config import ConfigFileParser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def set_search_engine():
    config_file = ConfigFileParser()
    email = config_file.FofaEmail()
    api_key = config_file.FofaToken()
    RulePorts = config_file.RulePorts()
    RuleHttpCode = config_file.RuleHttpCode()
    RulePortScanTimeout =config_file.RulePortScanTimeOut()
    RuleHttpTimeout = config_file.RuleHttpTimeOut()
    PathDeep = config_file.RulePathDeep()
    RuleExts = config_file.RuleExt()
    RuleYear = config_file.RuleYearDate()
    SCAN_RULES['http_code'] = [int(v.strip()) for v in RuleHttpCode.split(',')]
    SCAN_RULES['ports'] = [int(v.strip()) for v in RulePorts.split(',')]
    SCAN_RULES['http_timeout'] = float(RuleHttpTimeout)
    SCAN_RULES['portscan_timeout'] = float(RulePortScanTimeout)
    SCAN_RULES['path_deep'] = int(PathDeep)
    DICS_RULES['exts'] = [v.strip() for v in RuleExts.split(',')]
    DICS_RULES['year'] = RuleYear
    data = {'email':email,'api_key':api_key}
    SEARCH_ENG['FOFA'].update(data)
    return