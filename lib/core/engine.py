#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/8/22

from lib.core.data import conf
from lib.api.shodan.pack import shodan_query
from lib.api.fofa.pack import fofa_query
from lib.module.portScan.scanner import port_scan
from lib.utils.io import put_file_contents
import threading
import time
import queue
import traceback


def out(item, result_queue):
    if item:
        if len(item)> 1:
            if conf['www_scan']:
                urls_info = item[1:]
                for url,title in urls_info:
                    info = "{0}@ {1}".format(url,title)
                    put_file_contents('web_info.txt',info)
                    print(info)

            else:
                ports = list(set(item[1:]))
                data = item[0] + ':' + ','.join(ports)
                print(data)
                host = item [0]
                for port in ports:
                    status ,banner = port_scan(host,port)
                    if status == 'Open':
                        info = "{0}:{1} {2}|banner:{3}".format(host,port,status,banner)
                        put_file_contents('scan_port_info.txt',info)
                        print(info)

        pass


def run():
    task_queue = queue.Queue()
    out_queue = queue.Queue
    for host in conf['targets']:
        task_queue.put(host)
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
                target = self.task_queue.get(False)  # block= False
                if conf['api_mode'] == 'shodan':
                    info = shodan_query(target)
                if conf['api_mode'] == 'fofa':
                    info = fofa_query(target)
                host = [target]
                info = host + info

                self.task_handler(info, None, *self.args, **self.kwargs)
                self.task_queue.task_done()  # 退出queue
            except queue.Empty as e:
                break
            except Exception as e:
                print(traceback.format_exc())

            time.sleep(1)

    def stop(self):
        self.is_stoped = False