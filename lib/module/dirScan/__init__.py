#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/9/14

import asyncio
import aiohttp


def head_callback(task):
    print('This is callback')
    # 获取返回结果
    page_text = task.result()
    print(page_text)
    print("接下来就可以在回调函数中实现数据解析")


def get_callback(task):
    print('This is callback')
    # 获取返回结果
    (status,text) = task.result()
    print(status)
    print("接下来就可以在回调函数中实现数据解析")


async def get(url,timeout):
    async with aiohttp.ClientSession() as session:
        # 只要有耗时就会有阻塞，就得使用await进行挂起操作
        async with await session.get(url=url,timeout=timeout) as response:
            chunk = await response.content.read(200)
            status = response.status
            return (status,chunk)


async def head(url,timeout):
    async with aiohttp.ClientSession() as session:
        # 只要有耗时就会有阻塞，就得使用await进行挂起操作
        async with await session.head(url=url,timeout=timeout) as response:
            status = response.status
            return status


def search_file(urls,method,timeout):
    # 第一步产生事件循环对象
    loop = asyncio.get_event_loop()
    # 任务列表
    tasks = []
    for url in urls:
        if(method =="HEAD"):
            cone = head(url,timeout)
        if(method =="GET"):
            cone = get(url,timeout)
        task = asyncio.ensure_future(cone)
        # 给任务对象绑定回调函数用于解析响应数据
        task.add_done_callback(head_callback)
        # 第三步将所有的任务添加到任务列表中
        tasks.append(task)
    # 第四步运行事件循环对象，asyncio.wait()来实现多任务自动在循环中运行
    loop.run_until_complete(asyncio.wait(tasks))


def run_task(targets):

    return