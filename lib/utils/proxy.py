#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/11/2


import socks
import socket
import os


def set_proxy(proxy):
    proxy_type,_ = proxy.split(" ")
    host,port = _.split(":")
    if 'http'== proxy_type.lower():
        socks.set_default_proxy(socks.HTTP, host,int(port))
        socket.socket = socks.socksocket
    elif 'socks5' == proxy_type.lower():
        socks.set_default_proxy(socks.SOCKS5, host, int(port))
        socket.socket = socks.socksocket
    else:
        print("not supported the proxy type.")
        os._exit(0)
