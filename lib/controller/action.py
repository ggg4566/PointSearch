#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/7/9

from lib.core.enums import ACION
from lib.module.domainFind import get_domains
from lib.core.data import conf,SCAN_RESULT
from lib.module.getWeb.scan_port import port_scans
from lib.module.getWeb.aio_scan_port import port_scan
from lib.module.getWeb.scan_http import www_scan
from lib.module.wafCheck.identify_task import check_waf_scan
from lib.module.dirScan.init_dics import get_init_urls,get_sensive_urls
from lib.module.dirScan.file_scan import scan_file,sync_scan_file,async_scan_file
from lib.module.dirScan.dir_scan import scan_sensive_file
from lib.core.progress import create_bar
from lib.utils.common import list_file
from lib.utils.io import get_file_content,put_file_contents
import os
import threading
import time
import signal


def term_sig_handler(signum, frame):
    print('Ctrl + C !')
    os._exit(1)
    return


class background_thread(threading.Thread):
    def __init__(self,act):
        threading.Thread.__init__(self)
        self.act = act

    # 必须实现函数，run函数被start()函数调用
    def run(self):
        self.actin(self.act)
        return

    def actin(self,act):
        if act == ACION.WWWSCAN:
            targets = conf['targets']
            get_domains(targets)
            port_scan_nodes = port_scans()
            alive_web = www_scan(port_scan_nodes)
            bar = create_bar(range(len(alive_web)))
            check_waf_scan(alive_web)

        elif act == ACION.FILESCAN:
            urls = conf['targets']
            target_dics = get_init_urls(urls)
            bar = create_bar(range(len(target_dics)))
            num = 20000
            target_dics = [target_dics[i:i + num] for i in range(0, len(target_dics), num)]
            for v in target_dics:
                if conf['mode'] == 1:
                    sync_scan_file(v)
                else:
                    async_scan_file(v)
            print("\n\nPrint Scan Result:\n")
            for v in SCAN_RESULT['SCAN_FILE']:
                print(v)

        elif act == ACION.DIR_SCAN:
            urls = conf['targets']
            target_dics = get_sensive_urls(urls)
            bar = create_bar(range(len(target_dics)))
            num = 20000
            target_dics = [target_dics[i:i + num] for i in range(0, len(target_dics), num)]
            for v in target_dics:
                scan_sensive_file(v)
            #scan_sensive_file(target_dics)
            print("\n\nPrint Scan Result:\n")
            for v in SCAN_RESULT['SCAN_FILE']:
                print(v)
        elif act == ACION.RAD_SCAN:
            rad_path = "."
            while True:
                rad_path = input("Please input rad scan result path:")
                if not os.path.isdir(rad_path):
                    print("Please input a exist path")
                    continue
                else:
                    break
            url_files = list_file(rad_path, ['.path'])
            if url_files:
                for file in url_files:
                    urls = get_file_content(file)
                    if urls:
                        print("Start urls from %s" % file)
                        target_dics = get_init_urls(urls)
                        bar = create_bar(range(len(target_dics)))
                        num = 20000
                        target_dics = [target_dics[i:i + num] for i in range(0, len(target_dics), num)]
                        for v in target_dics:
                            scan_file(v)
                        target_dics = get_sensive_urls(urls)
                        bar = create_bar(range(len(target_dics)))
                        num = 20000
                        target_dics = [target_dics[i:i + num] for i in range(0, len(target_dics), num)]
                        for v in target_dics:
                            scan_sensive_file(v)
                print("\n\nPrint Scan Result:\n")
                for v in SCAN_RESULT['SCAN_FILE']:
                    print(v)
            else:
                print("Nothint not found for ext is '.path' ")
        elif act == ACION.CHECK_WAF:
            urls = conf['targets']
            bar = create_bar(range(len(urls)))
            check_waf_scan(urls)
            print("\n\nPrint Identify Result:\n")
            for v in SCAN_RESULT['SCAN_FILE']:
                print(v)
        for v in SCAN_RESULT['SCAN_FILE']:
            put_file_contents(conf['out_file'], v)
        return


def actin(act):
    signal.signal(signal.SIGINT, term_sig_handler)
    t = background_thread(act)
    t.setDaemon(True)
    t.start()

    while True:
        if not t.is_alive():
            break
        time.sleep(3)
    return