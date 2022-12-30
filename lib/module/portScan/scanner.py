#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/9/10
import socket
from lib.core.data import  SCAN_RULES

def port_scan(host,port):
    status = "closed"
    banner = ""
    timeout = SCAN_RULES['portscan_timeout']
    socket.setdefaulttimeout(timeout)
    port = int(port)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if s.connect_ex((host, port)) == 0:
            status = "Open"
    except Exception as e:
        pass
    finally:
        s.close()
    if status == "Open":
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send(b'HELLO\r\n')
            banner = s.recv(100)
        except Exception as e:
            pass
        finally:
            s.close()
    return status,banner

