#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/7/19

from lib.core.data import conf,logger,SCAN_RULES,SCAN_RESULT
from lib.core.enums import REQUEST_METHOD
from lib.api.fofa.pack import fofa_query
from lib.module.findFile import search_file
from lib.module.portScan.scanner import port_scan
from lib.utils.io import put_file_contents


import threading
import time
import queue
import traceback


def out(item, result_queue):
    logger.success(item)
    return


def init_scan_task(targets):
    ret = []
    for t in targets:
        for port in SCAN_RULES['ports']:
            ret.append({'target':t,'port':port})
    return ret


def port_scans():
    target_node = []
    ret = []
    for __ in SCAN_RESULT['RAPID_DNS']:
        for node in __:
            target_node.append(node["name"])
    for __ in SCAN_RESULT['FOFA_RESULT']:
        for node in __:
            if(node[0].startswith("http")):
                domain = node[0].split(r'//')[1]
                target_node.append(domain)
            else:
                target_node.append(node[0])

    target_node=list(set(target_node))
    tasks = init_scan_task(target_node)
    task_queue = queue.Queue()
    out_queue = queue.Queue()
    for task in tasks:
        task_queue.put(task)
    ScanHandler(task_queue, out, out_queue, conf['thread_num']).run()

    while True:
        scan_info = out_queue.get()
        banner =str(scan_info['banner'])
        if (scan_info['status'] == 'Open' and 'HTTP' in banner):
            ret.append(scan_info)
        if out_queue.empty():
            break

    return ret


class ScanHandler(object):
    def __init__(self, task_queue, task_handler, result_queue=None, thread_count=1, *args, **kwargs):
        self.task_queue = task_queue
        self.task_handler = task_handler
        self.result_queue = result_queue
        self.thread_count = thread_count
        self.args = args
        self.kwagrs = kwargs
        self.thread_pool = []

    def run(self):
        for i in range(self.thread_count):
            t = _TaskHandler(self.task_queue, self.task_handler, self.result_queue, *self.args, **self.kwagrs)
            self.thread_pool.append(t)
        for th in self.thread_pool:
            th.setDaemon(True)
            th.start()

        while self._check_stop():
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print('KeyboardInterruption')
                self.stop_all()
                break
        logger.info('>>>Scan port Finshed.')

    def _check_stop(self):
        finish_num = 0
        for th in self.thread_pool:
            if not th.is_alive():
                finish_num += 1

        return False if finish_num == len(self.thread_pool) else True

    def stop_all(self):
        for th in self.thread_pool:
            th.stop()


class _TaskHandler(threading.Thread):

    def __init__(self, task_queue, task_handler, result_queue=None, *args, **kwargs):
        threading.Thread.__init__(self)
        self.task_queue = task_queue
        self.task_handler = task_handler
        self.result_queue = result_queue
        self.args = args
        self.kwargs = kwargs
        self.is_stoped = True

    def run(self):
        while self.is_stoped:
            try:
                info=None
                target = self.task_queue.get(False)  # block= False

                    #info = fofa_query(target)
                host = target['target']
                port = target['port']
                status,banner = port_scan(host,port)
                # info = "{0}:{1}@{2}:{3}".format(host,port,status,banner)
                info = {'host':host,'port':port,'status':status,'banner':banner}
                #info = search_file(target,REQUEST_METHOD.HEAD,5)
                self.result_queue.put(info)
                self.task_handler("{0}:{1} {2}".format(host,port,status), self.result_queue, *self.args, **self.kwargs)
                self.task_queue.task_done()  # 退出queue
            except queue.Empty as e:
                break
            except Exception as e:
                print(traceback.format_exc())

            time.sleep(1)

    def stop(self):
        self.is_stoped = False