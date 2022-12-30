#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/9/16


from urllib import parse
from lib.module.fuzzDics import get_custom_file_dics,get_path_dics,get_sensive_dics,get_dir_dics
from lib.core.data import SCAN_RULES,DICS_RULES
TARGET_DIR_NODE = {'target':"",
               'Path':[]
               }
DIR_DICS = {"host":"","target":"","paths":[]}
#target_nodes ={}

def parse_url(url):
    _ = parse.urlparse(url)
    scheme = _.scheme
    netloc = _.netloc
    path = _.path
    url = "{0}://{1}".format(scheme,netloc)
    return (netloc,url,path)


def get_all_path(paths,dir_deeps=3): # get sitemap path
    dirs = []
    nodes = []
    for path in paths:
        __ = path.split("/")
        tmp = []
        for _ in __:
            if _ !='':
                tmp.append(_)
        if tmp:
            nodes.append(tmp)

    for node in nodes:
        length = len(node)
        for i in range(length):
            if i+1 <=dir_deeps:
                dirs.append("/".join(node[0:i+1]))
    dirs =list(set(dirs))
    return dirs


def get_sitemap(urls):
    target_nodes = {}
    for url in urls:
        ret = parse_url(url)
        target_node = {}
        host = ret[0]
        target_node["host"] = ret[0]
        if host in target_nodes.keys():
             target_nodes.get(host).get('paths').append(ret[2])
        else:
            target_node["host"] = ret[0]
            target_node["target"] = ret[1]
            target_node["paths"] =[]
            target_node["paths"].append(ret[2])
            Node = {host:target_node}
            target_nodes.update(Node)
        l = []
        l = list(set(target_nodes.get(host).get('paths')))
        target_nodes.get(host).update({'paths':l})
    return target_nodes


urls = ["http://www.baidu.com/path/index.php",
        "http://www.qq.com/path",
        "http://www.baidu.com/path/test/",
        "http://www.baidu.com/path/test/good/xxx",
        "http://www.baidu.com/aa/g/d",
        "http://www.baidu.com/path/g",
        "http://www.baidu.com/aa/c",
        "http://www.baidu.com/",
        "http://www.baidu.com",
        ]

def get_init_urls(urls):
    #urls = [url+'/' for url in urls]
    ret = []
    target_nodes = get_sitemap(urls)
    keys = target_nodes.keys()
    for key in keys:
        l = target_nodes.get(key).get('paths')
        l += get_dir_dics()
        l = list(set(l))
        path_map = get_all_path(l, SCAN_RULES['path_deep'])
        custom_dics = get_custom_file_dics(key)
        target = target_nodes.get(key).get('target')
        path_dics = get_path_dics(path_map)
        for path in path_map:
                v = path +'/' + key
                file_exts = DICS_RULES['exts']
                for ext in file_exts:
                    var = "/{0}.{1}".format(v, ext)
                    path_dics.append(var)
        target_dics= list(set(custom_dics+path_dics))
        __ =  [target+'/'+v for v in target_dics]
        ret+= __
    return ret


def get_sensive_urls(urls):
    ret = []
    target_nodes = get_sitemap(urls)
    keys = target_nodes.keys()
    for key in keys:
        l = target_nodes.get(key).get('paths')
        l = list(set(l))
        path_map = get_all_path(l, SCAN_RULES['path_deep'])
        target = target_nodes.get(key).get('target')
        __ = [target + '/' + v for v in path_map]
        ret += __
        ret = list(set(ret))
    target_dics = []
    sensive_files = get_sensive_dics()
    if ret:
        for t in ret:
            for f in sensive_files:
                target_dics.append(t + f)
        ret =target_dics
    else:
        for url in urls:
            for f in sensive_files:
                target_dics.append(url + f)
        ret = target_dics
    return ret


def get_init_url(url):
    ret = []
    data = parse_url(url)
    host = data[0]
    target = data[1]
    custom_dics = get_custom_file_dics(host)
    ret = [target+'/'+v for v in custom_dics]
    return ret


def get_targets(urls):
    ret = []
    target_nodes = get_sitemap(urls)
    keys = target_nodes.keys()
    for key in keys:
        target = target_nodes.get(key).get('target')
        ret.append(target)
    return ret