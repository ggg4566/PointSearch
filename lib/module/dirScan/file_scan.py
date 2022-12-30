#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/9/22
from lib.module.dirScan.init_dics import get_init_urls,get_targets
from lib.common.ithreadpool import SyncThreadHandle,user_lock
from lib.common.request.sync_request import get_request_client
from lib.common.request.async_request import get_arequest_client
from lib.module.fuzzDics import get_dir_dics
from lib.utils.io import read_file_con
from lib.core.data import logger,COLOR,SCAN_RULES,SCAN_RESULT,conf
from lib.core.progress import print_progress,create_bar
from lib.utils.http import get_ua
import asyncio
import aiohttp
import json
import traceback


def check_file_exist(buffer):
    hex_magics  = buffer.hex()
    ret = False
    con = read_file_con("magic.txt")
    dict= json.loads(con)
    for value in dict.values():
        is_find = False
        if "," in value:
            l = value.split(",")
            for v in l:
                w_l = len(v)
                if(v == hex_magics[0:w_l]):
                    is_find = True
                    break

        else:
            w_l = len(value)
            if (value == hex_magics[0:w_l]):
                is_find = True
        if(is_find == True):
            ret = is_find
            break
    return ret

# 回调函数: 主要用来解析响应数据
def callback(task):
    # 获取响应数据
    try:
        url, status, page_text = task.result()
        if(status == 200):
            is_found = check_file_exist(page_text)
            if is_found:
                success_info = r"{0}".format(COLOR['red']+"{0}|{1}".format(url,status)+COLOR['general'])
                logger.success(success_info)
                SCAN_RESULT['SCAN_FILE'].append(success_info)
    except Exception:
        pass

    print_progress(1)


async def fetch(session, url):

    try:
        headers = {'User-Agent': get_ua()}
        async with session.get(url, headers=headers, verify_ssl=False) as resp:
            return url,resp.status, await resp.content.read(20)
    except aiohttp.ServerTimeoutError:
        #print(f" url: {url} error happened:")
        #logger.error("%s Connection timeout"%url)
        pass
    except Exception:
        #print(traceback.format_exc())
        #logger.error("%s request error"%url)
        pass


async def fetch_all(urls):
    '''
    urls: list[(id_, url)]
    '''
    connector = aiohttp.TCPConnector(limit=conf['thread_num'],verify_ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for  url in urls:
            # 在Python3.7+，asyncio.ensure_future() 改名为 asyncio.create_task()
            task = asyncio.ensure_future(fetch(session, url))
            task.add_done_callback(callback)
            tasks.append(task)
        datas = ""
        await asyncio.gather(*tasks, return_exceptions=True)
        # return_exceptions=True 可知从哪个url抛出的异常
        '''
        for ind, data in enumerate(urls):
            url = dataPointSearch.py -l https://www.westernmassnews.com/Apps_Plugins/ -a 2
 
            if isinstance(datas[ind], Exception):
                pass
                #do_again(session,url)
                #print(f"{url}: ERROR")
                #task = asyncio.ensure_future(fetch(session, url))
                #task.add_done_callback(callback)
        '''
        return datas


def scan_file(target_dics):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fetch_all(target_dics))
    #loop.close()
    return


def check_file(url,tup_params):
    user_lock.acquire()
    print_progress(1)
    user_lock.release()
    RequestClient = tup_params[0]
    try:
        with RequestClient.stream("GET", url) as r:
            status = r.status_code
            try:
                if status == 200 and 'text/html' not in r.headers["Content-Type"] and 'text/plain' not in r.headers["Content-Type"] and 'application/json' not in r.headers["Content-Type"] and 'image/jpeg' not in r.headers["Content-Type"]:
                    chunk_data = r.iter_raw(20)
                    for chunk in chunk_data:
                        is_found = check_file_exist(chunk)
                        if is_found:
                            success_info = r"{0}".format(
                                COLOR['red'] + "{0}|{1}".format(url, status) + COLOR['general'])
                            logger.success(success_info)
                            user_lock.acquire()
                            SCAN_RESULT['SCAN_FILE'].append(success_info)
                            user_lock.release()
                        raise StopIteration
            except StopIteration:
                chunk_data.close()
            except Exception:
                #print(traceback.format_exc())
                #print("%s error" % url)
                pass
    except Exception:
        '''
        print(traceback.format_exc())
        print("%s error"%url)
        '''
        pass


async def httpx_fetch(RequestClient,sem,url):
    try:
        async with sem:
            async with RequestClient.stream('GET', url) as r:
                print_progress(1)
                status = r.status_code
                chunks  = r.aiter_raw(20)
                try:
                    async for chunk in chunks:
                        data = chunk
                        if status == 200 and 'text/html' not in r.headers["Content-Type"] and 'text/plain' not in \
                                r.headers["Content-Type"] and 'application/json' not in r.headers[
                            "Content-Type"] and 'image/jpeg' not in r.headers["Content-Type"]:
                            is_found = check_file_exist(data)
                            if is_found:
                                success_info = r"{0}".format(
                                    COLOR['red'] + "{0}|{1}".format(url, status) + COLOR['general'])
                                logger.success(success_info)
                                SCAN_RESULT['SCAN_FILE'].append(success_info)
                        break
                finally:
                    await chunks.aclose()  #

    except Exception:
        print(traceback.format_exc())
    return


async def httpx_fetch_all(urls,RequestClient,sem):
    async with RequestClient as session:
        tasks = []
        for url in urls:
            # 在Python3.7+，asyncio.ensure_future() 改名为 asyncio.create_task()
            task = asyncio.ensure_future(httpx_fetch(session,sem,url))
            # task.add_done_callback(acheck_url)
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


def sync_scan_file(target_dics):
    RequestClient = get_request_client()
    pool_task = SyncThreadHandle(target_dics, check_file, conf['thread_num'],RequestClient)
    pool_task.run()
    pool_task.wait_finsh()
    RequestClient.close()
    return


def async_scan_file(target_dics):

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    RequestClient = get_arequest_client()
    sem = asyncio.Semaphore(conf['thread_num'])
    loop.run_until_complete(httpx_fetch_all(target_dics,RequestClient,sem))
    RequestClient.aclose()
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
