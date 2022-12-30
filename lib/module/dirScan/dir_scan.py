#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/9/22
from lib.module.dirScan.init_dics import get_targets
from lib.module.fuzzDics import get_dir_dics
from lib.core.data import logger,COLOR,SCAN_RULES,SCAN_RESULT,conf
from lib.core.progress import print_progress
from lib.utils.http import get_ua
import asyncio
import aiohttp
import traceback
import platform
headers = {
    'User-Agent': get_ua()}
# 回调函数: 主要用来解析响应数据
def callback(task):
    # 获取响应数据
    try:
        url,status = task.result()
        codes = SCAN_RULES['http_code']
        if(status in codes):
            success_info = r"{0}".format(COLOR['red'] + "{0}|{1}".format(url, status) + COLOR['general'])
            logger.success(success_info)
            SCAN_RESULT['SCAN_FILE'].append(success_info)
    except Exception:
        #print(traceback.format_exc())
        pass
    print_progress(1)


async def fetch(session, url):
    try:
        async with session.get(url, headers=headers, verify_ssl=False) as resp:
            return url,resp.status
    except Exception:

        #print(traceback.format_exc())
        print("%s request error"%url)


async def fetch_all(urls):
    '''
    urls: list[(id_, url)]
    '''
    connector = aiohttp.TCPConnector(limit=conf['thread_num'],verify_ssl=False,force_close=True)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for  url in urls:
            # 在Python3.7+，asyncio.ensure_future() 改名为 asyncio.create_task()
            task = asyncio.ensure_future(fetch(session, url))
            task.add_done_callback(callback)
            tasks.append(task)
        datas = await asyncio.gather(*tasks, return_exceptions=True)
        return datas
        # return_exceptions=True 可知从哪个url抛出的异常
        '''
        for ind, data in enumerate(urls):
            url = data
            if isinstance(datas[ind], Exception):
                print(f"{url}: ERROR")
        return datas
        '''


def scan_sensive_file(target_dics):
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_all(target_dics))
    return


def scan_dir(urls):
    ret = []
    targets = get_targets(urls)
    dirs = get_dir_dics()
    for target in targets:
        for dir in dirs:
            print(dir)
            ret.append(dir)
    return ret
