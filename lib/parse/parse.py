#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/8/22

from optparse import OptionParser
import sys


def parse_cmd_line():
    usage = "usage: %prog [options] -l domain [-L domains.txt] -a [1,2,3]"
    parser = OptionParser(usage)
    parser.add_option("-l", "--host", dest="domain",action="store",
                      help="set scan target. ", metavar="domain")
    parser.add_option("-L", "--file",dest="file",
                      action="store", help="load targets form file.", metavar="target")
    parser.add_option("-t", "--threads", dest="thread_num",default = 10,type=int,
                      action="store", help="set thread numbers,default valuse is 10.", metavar="thread_nums")
    parser.add_option("-m", "--mode", dest="mode", type=int, default = 1,
                      action="store", help='''set do request mode. default set 1
                                        choice 1 set syncio  mode
                                        choice 2 set asyncio mode
                      ''')

    parser.add_option("-a","--action", dest="action",type=int,
                      action="store", help='''set do action.            
                                        choice 1 do --get-www auto search web of no protection by fofa and rapiddns.
                                        choice 2 do --scan-file
                                        choice 3 do --scan-dir
                                        choice 4 do --scan-all-files from path import rad spider result.
                                        choice 5 do --check-waf
                        ''')
    parser.add_option("--proxy", dest="proxy",action="store",
                      help="set global proxy. http 127.0.0.1:8080 or socks5 127.0.0.1:1080 ", metavar="proxy")
    parser.add_option("-o", "--out",dest="out",
                      action="store", help="save scan result to file.", metavar="out-file",default="scan_result.txt")
    (options, args) = parser.parse_args()
    if (not options.domain and not options.file) or (not options.action):
        parser.print_help()
        sys.exit()

    return options