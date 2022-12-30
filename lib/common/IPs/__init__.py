#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/8/20
import re


def ip2num(ip):
    ip=[int(x) for x in ip.split('.')]
    return ip[0] <<24 | ip[1]<<16 | ip[2]<<8 |ip[3]


def num2ip(num):
    return '%s.%s.%s.%s' %( (num & 0xff000000) >>24,
                            (num & 0x00ff0000) >>16,
                            (num & 0x0000ff00) >>8,
                            num & 0x000000ff )
def get_ip(ip):
    start,end = [ip2num(x) for x in ip.split('-') ]
    return [ num2ip(num) for num in range(start,end+1) if num & 0xff ]


def is_ip(str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False


def get_ipaddr(ips):
    iplist = get_ip(ips)
    return iplist