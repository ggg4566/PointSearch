#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/7/12
from lib.core.data import conf,logger,SCAN_RULES
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


def run_file_scan():
    task_queue = queue.Queue()
    out_queue = queue.Queue()
    if(len(conf['file_dics'])>0):
        for host in conf['targets']:
            for dic in conf['file_dics']:
                task_queue.put("{0}{1}".format(host,dic))
        ScanHandler(task_queue, out, out_queue, conf['thread_num']).run()

    return


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
        print('>>>ALL Task Finshed.')

    def _check_stop(self):
        finish_num = 0
        for th in self.thread_pool:
            if not th.isAlive():
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
                time_out  =SCAN_RULES['http_timeout']
                info = search_file(target,REQUEST_METHOD.HEAD,time_out)
                if info == 200:
                    self.task_handler("{0} || {1}".format(target,info), None, *self.args, **self.kwargs)
                self.task_queue.task_done()  # 退出queue
            except queue.Empty as e:
                break
            except Exception as e:
                print(traceback.format_exc())

            time.sleep(1)

    def stop(self):
        self.is_stoped = False