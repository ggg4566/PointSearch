#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/10/25

from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED
import threading
user_lock=threading.Lock()

class SyncThreadHandle(object):
    def __init__(self, targets, task_handler,thread_count=1, *args):
        self.targets = targets
        self.task_handler = task_handler
        self.thread_count = thread_count
        self.args = args
        self.tasks = []
        self.is_stop = False
        self.pool = ThreadPoolExecutor(max_workers=self.thread_count)

    def run(self):
        self.control_submit_speed()

    def stop(self):
        is_stop = True
        wait(self.tasks, return_when=ALL_COMPLETED)
        self.pool.shutdown()


    def control_submit_speed(self):
        counts = len(self.targets)
        task_queue_size = self.thread_count*100
        i = 0
        loop = 0
        while True:
            if loop < task_queue_size:
                try:
                    self.tasks.append(self.pool.submit(self.task_handler,self.targets[i], self.args))
                except RuntimeError:
                    return
                except Exception:
                    pass
                i = i+1
                loop = loop+1
                if(loop == task_queue_size):
                    loop = 0
            if i == counts:
                break
        return

    def wait_finsh(self):
        wait(self.tasks, return_when=ALL_COMPLETED)
        self.pool.shutdown()
        return