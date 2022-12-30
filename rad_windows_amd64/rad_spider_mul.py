#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/10/22


import subprocess
import warnings
import random
import sys
import optparse

ua = "test"
warnings.filterwarnings(action='ignore')
from urllib import parse


def url2host(url):
    _ = parse.urlparse(url)
    netloc = _.netloc
    return netloc


def get_file_content(filename):
    result = []
    f = open(filename, "r")
    for line in f.readlines():
        if line:
            result.append(line.strip())
    f.close()
    return result


def main():
    commandList = optparse.OptionParser('usage: %prog -u target [-f file] -p rad spider path')
    commandList.add_option('-u', '--url', action="store",
                           help="Insert TARGET URL: http[s]://www.victim.com[:PORT]",
                           )
    commandList.add_option('-f', '--file', action='store',
                           help='Insert filename of stored target ::')
    commandList.add_option('-p', '--path', action="store",
                           help="rad path",
                           )
    options, remainder = commandList.parse_args()
    if ((not options.file) and (not options.url)) or not options.path :
        commandList.print_help()
        sys.exit(1)
    targets = [options.url] if options.url else get_file_content(options.file)
    rad_path = options.path
    for target in targets:
        try:
            out = "{0}_{1}.rad".format(url2host(target),random.randrange(2000))
            print(out)
            #cmd = ["/opt/rad/rad_linux_amd64", "-t", target, "--json", out]
            cmd = [r"%s"% rad_path, "-t", target, "--json", out]
            rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = rsp.communicate()
            print(output)
            print("[%s] done."% target)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
        main()
