#! /usr/bin/env python
# -*- coding:utf-8 -*-
# author:flystart
# home:www.flystart.org
# time:2021/10/21

import random

def get_ua():
    agents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) " +
        "Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0)" +
        " Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; " +
        "Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS " +
        "X 10_12_2) AppleWebKit/602.3.12 (KHTML, " +
        "like Gecko) Version/10.0.2 Safari/602.3.12",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; " +
        "rv:51.0) Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 " +
        "like Mac OS X) AppleWebKit/602.4.6 (KHTML, " +
        "like Gecko) Version/10.0 Mobile/14D27" +
        " Safari/602.1",
        "Mozilla/5.0 (Linux; Android 6.0.1; " +
        "Nexus 6P Build/MTC19X) AppleWebKit/537.36 " +
        "(KHTML, like Gecko) Chrome/56.0.2924.87 " +
        "Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 " +
        "Build/KTU84P) AppleWebKit/537.36 (KHTML, " +
        "like Gecko) Chrome/56.0.2924.87" +
        "Mobile Safari/537.36",
        "Mozilla/5.0 (compatible; Googlebot/2.1; " +
        "+http://www.google.com/)"
    ]
    return random.choice(agents)