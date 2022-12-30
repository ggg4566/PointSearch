#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/7/9

from lib.module.domainFind.fofa import fofa_query
from lib.module.domainFind.rapiddns import rapid_query
from lib.core.data import logger,SCAN_RESULT


def get_domains(targets):
    for target in targets:
        res = []
        try:
            logger.info("Start get domains by FOFA!")
            res = fofa_query(target)
            if res:
                SCAN_RESULT['FOFA_RESULT'].append(res)
            logger.success("Finshed get domains by FOFA! get subdomain %s number." % len(res))
            # for __ in SCAN_RESULT['FOFA_RESULT']:
            #     for node in __:
            #         logger.success("{0}|{1}|{2}".format(node[0],node[1],node[2]))

            res = []
            logger.info("Start get domains by RapidDNS!")
            res = rapid_query(target)
            if res:
                SCAN_RESULT['RAPID_DNS'].append(res)
            logger.success("Finshed get domains by RapidDNS! get subdomain %s number." % len(res))
            res = []
            # for __ in SCAN_RESULT['RAPID_DNS']:
            #     for node in __:
            #         logger.success("{0}|{1}".format(node["name"],node["value"]))

        except Exception as e:
            logger.error(e)
        logger.info("get domains end!")
    return