#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/10/20


import optparse
import sys,os
import json
from urllib import parse
from typing import List



def list_file(path):
    filters = ['.rad']
    ret = []
    filelist=os.listdir(path)
    for filename in filelist:
        fpath=os.path.join(path,filename)
        if os.path.isdir(fpath):
            list_file(fpath)
        if not os.path.isdir(fpath) and os.path.splitext(fpath)[1] in filters:
            ret.append(fpath)
    return ret


def findjsonobject(JsonPathFinderobject, pathlist):   # 由地址找对象
    jsondata = JsonPathFinderobject.data
    data_result = jsondata.copy()
    for step in pathlist:
        data_result = data_result[step]
    return data_result


class JsonPathFinder:
    def __init__(self, json_str):
        self.data = json.loads(json_str)

    def iter_node(self, rows, road_step, target):
        if isinstance(rows, dict):
            key_value_iter = (x for x in rows.items())
        elif isinstance(rows, list):
            key_value_iter = (x for x in enumerate(rows))
        else:
            return
        for key, value in key_value_iter:
            current_path = road_step.copy()
            current_path.append(key)
            if key == target:
                yield current_path
            if isinstance(value, (dict, list)):
                yield from self.iter_node(value, current_path, target)

    def find_one(self, key: str) -> list:
        path_iter = self.iter_node(self.data, [], key)
        for path in path_iter:
            return path
        return []

    def find_all(self, key) -> List[list]:
        path_iter = self.iter_node(self.data, [], key)
        return list(path_iter)

    def iter_node2(self, rows, road_step, target):   # 我瞎写的查找value的函数
        if isinstance(rows, dict):
            key_value_iter = (x for x in rows.items())
        elif isinstance(rows, list):
            key_value_iter = (x for x in enumerate(rows))
        else:
            return
        for key, value in key_value_iter:
            current_path = road_step.copy()
            current_path.append(key)
            if value == target:   # 只查找value
                yield current_path
            if isinstance(value, (dict, list)):
                yield from self.iter_node2(value, current_path, target)

    def find_one_value(self, targetvalue: str) -> list:
        path_iter = self.iter_node2(self.data, [], targetvalue)
        for path in path_iter:
            return path
        return []

    def find_all_value(self, targetvalue) -> List[list]:
        path_iter = self.iter_node2(self.data, [], targetvalue)
        return list(path_iter)


def put_file_contents(filename,contents):
    with open(filename,"a+") as fin:
        fin.write(contents+"\n")


def get_file_content(filename):
    contents=""
    with open(filename,"r") as fin:
        contents=fin.read()
    return contents


def get_json_value_by_key(self, in_json, target_key, results=[]):

    return results


def url2Path(url):
    _ = parse.urlparse(url)
    scheme = _.scheme
    netloc = _.netloc
    path = _.path
    url = "{0}://{1}/".format(scheme,netloc)
    return url,path


def get_path_dics(url):
    ret =url
    host,path = url2Path(url)
    _ = path.split("/")
    d = _[:-1]
    __ = "/".join(d)
    ret = host+ __
    return ret


def parse_path_from_rad_resulst(filename):
    key = "URL"
    return parse_result_form_json(filename,key)


def parse_result_form_json(filename,key):
    ret = []
    json_text = get_file_content(filename)
    finder = JsonPathFinder(json_text)
    path_list = finder.find_all(key)
    _ = finder.data
    res = []
    for path in path_list:
        d = _[path[0]]
        v = d.get(key)
        url = get_path_dics(v)
        res.append(url)
    __ = list(set(res))
    ret += __
    return ret

def main():
    commandList = optparse.OptionParser('usage: %prog [-f store hosts file ]')
    commandList.add_option('-f', '--file', action='store',
                           help='Insert filename of stored hosts')
    commandList.add_option('-k', '--key', action="store",
              help="provide json key",
            )
    commandList.add_option('-m', '--mode', action="store",type=int,
              help=r'''function mode.
              
                    choice 1 , parse json data form json file by json key
                    choice 2 , parse all url from rad spider resulst.,at moment -f is os path 
              '''
            )
    options, remainder = commandList.parse_args()
    if ((not options.file) and (not options.key)) or not options.mode:
        commandList.print_help()
        sys.exit(1)

    key = options.key
    filename = options.file
    mode = options.mode
    if mode == 1:
        __ = parse_result_form_json(filename,key)
        for _ in __:
            v = _
            print(v)
            put_file_contents("json_result.txt",v)
    elif mode == 2:
        if not os.path.isdir(filename):
            print("Please provide a exist path by -f ")
            return
        out_path ="{0}{1}parse_out{2}".format(filename,os.sep,os.sep)
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        rad_files = list_file(filename)
        for file in rad_files:
            __ = parse_path_from_rad_resulst(file)
            for _ in __:
                v = _
                print(v)
                fpath, fname = os.path.split(file)
                put_file_contents(out_path+fname+".path", v)



if __name__ == "__main__":
    main()