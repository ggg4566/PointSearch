#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2020/8/20


from lib.core.option import init_options
from lib.core.data import conf,COLOR,logger
from lib.controller.action import actin
import os
import warnings
warnings.filterwarnings("ignore")


def main():
    conf['root_path'] = os.path.dirname(os.path.realpath(__file__))
    init_options()
    act = conf['action']
    actin(act)



if __name__ == '__main__':
    banner = r''' 
    
    ____        _       __     _____                      __  
   / __ \____  (_)___  / /_   / ___/___  ____ ___________/ /_ 
  / /_/ / __ \/ / __ \/ __/   \__ \/ _ \/ __ `/ ___/ ___/ __ \
 / ____/ /_/ / / / / / /_    ___/ /  __/ /_/ / /  / /__/ / / /
/_/    \____/_/_/ /_/\__/   /____/\___/\__,_/_/   \___/_/ /_/ 
                                                              
                                                  
    '''
    info =r'''
    version:1.0.0
    author:flystart
    mail:root@flystart.org
    '''
    print(COLOR['blue'] + banner + COLOR['white'] + info + COLOR['general'])

    main()
