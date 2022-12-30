#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2022/1/19
import asyncio
import sys
from socket import socket, AF_INET, SOCK_STREAM
import time
from asyncio import Queue, TimeoutError, gather
from typing import List
from async_timeout import timeout
from lib.core.data import conf,logger,SCAN_RULES,SCAN_RESULT


port_founds = []
def init_scan_task(targets):
    ret = []
    for t in targets:
        for port in SCAN_RULES['ports']:
            ret.append((t,port))
    return ret


class ScanPort(object):
    def __init__(self, time_out: float = 0.1, task_list: List[tuple] = None, concurrency: int = 500):
        self.task_list = task_list
        self.result: List[int] = []
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.loop = loop
        # 队列的事件循环需要用同一个，如果不用同一个会报错，这里还有一点不明白
        self.queue = Queue(loop=self.loop)
        self.timeout = time_out
        # 并发数
        self.concurrency = concurrency

    @staticmethod
    def get_event_loop():
        """
        判断不同平台使用不同的事件循环实现

        :return:
        """
        if sys.platform == 'win32':
            from asyncio import ProactorEventLoop
            # 用 "I/O Completion Ports" (I O C P) 构建的专为Windows 的事件循环
            return ProactorEventLoop()
        else:
            from asyncio import SelectorEventLoop
            return SelectorEventLoop()

    async def scan(self):
        while True:
            t1 = time.time()
            task_node = await self.queue.get()
            sock = socket(AF_INET, SOCK_STREAM)

            try:
                with timeout(self.timeout):
                    # 这里windows和Linux返回值不一样
                    # windows返回sock对象，Linux返回None
                    await self.loop.sock_connect(sock, task_node)
                    t2 = time.time()
                    # 所以这里直接直接判断sock
                    if sock:
                        self.result.append(task_node)
                        info = task_node[0]+'@'+str(task_node[1])+'@open'
                        logger.info(info)
                        port_founds.append((task_node[0],task_node[1]))

            # 这里要捕获所有可能的异常，windows会抛出前两个异常，Linux直接抛最后一个异常
            # 如果有异常不处理的话会卡在这
            except (TimeoutError, PermissionError, ConnectionRefusedError) as _:
                sock.close()
            sock.close()
            self.queue.task_done()

    async def start(self):
        start = time.time()
        if self.task_list:
            for a in self.task_list:
                self.queue.put_nowait(a)
        task = [self.loop.create_task(self.scan()) for _ in range(self.concurrency)]
        # 如果队列不为空，则一直在这里阻塞
        await self.queue.join()
        # 依次退出
        for a in task:
            a.cancel()
        # Wait until all worker tasks are cancelled.
        await gather(*task, return_exceptions=True)


def port_scan():
    ret = []
    target_node = []
    ret = []
    for __ in SCAN_RESULT['RAPID_DNS']:
        for node in __:
            target_node.append(node["name"])
    for __ in SCAN_RESULT['FOFA_RESULT']:
        for node in __:
            if (node[0].startswith("http")):
                domain = node[0].split(r'//')[1]
                target_node.append(domain)
            else:
                target_node.append(node[0])

    target_node = list(set(target_node))
    task_list = init_scan_task(target_node)

    scan = ScanPort(time_out=SCAN_RULES['portscan_timeout'],task_list=task_list,concurrency=500)
    scan.loop.run_until_complete(scan.start())
    logger.info('>>>Scan port Finshed.')
    for v in port_founds:
        info = {'host': v[0], 'port': v[1]}
        ret.append(info)
    return ret

