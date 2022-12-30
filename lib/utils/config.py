#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/8/22

import configparser
from lib.core.data import conf
import os


class ConfigFileParser(object):
    @staticmethod
    def _get_option(section, option):
        try:
            cf = configparser.ConfigParser()
            cf.read(os.path.join(conf['root_path'],'config.conf'))
            return cf.get(section=section, option=option)
        except configparser.NoOptionError as e:
            print('Missing essential options, please check your config-file.')
            print(e)
            return ''

    def FofaEmail(self):
        return self._get_option('fofa', 'email')

    def FofaToken(self):
        return self._get_option('fofa', 'api_key')

    def ShodanApikey(self):
        return self._get_option('shodan', 'api_key')

    def RulePorts(self):
        return self._get_option('scan_rule', 'ports')

    def RuleHttpCode(self):
        return self._get_option('scan_rule', 'http_code')

    def RulePortScanTimeOut(self):
        return self._get_option('scan_rule', 'portscan_timeout')

    def RuleHttpTimeOut(self):
        return self._get_option('scan_rule', 'http_timeout')

    def RulePathDeep(self):
        return self._get_option('scan_rule', 'path_deep')

    def RuleExt(self):
        return self._get_option('dics_rule', 'ext')

    def RuleYearDate(self):
        return self._get_option('dics_rule', 'date_year')