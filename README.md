- [说明](#--)
- [使用](#--)
    + [配置](#--)
    + [扫描备份文件](#------)
    + [Rad爬虫递归扫描](#rad------)
    + [扫描敏感文件](#------)
# 说明

本工具主要用来批量扫描网站的备份文件。相比于一般的备份文件扫描工具，具有以下特色：

1.速度快。使用了异步IO和线程池两种模式，扫描文件使用了魔术头字符串来判断，不需要请求下载整个文件，速度还是挺给力的，可根据自己带宽设置合理的并发数

2.大批量目标快速扫描

3.结合rad爬虫递归目录扫描

4.域名、date等内置字典规则

其他，还实现了子域名收集（rapidns、fofa）比较鸡肋、checkwaf功能

<img width="757" alt="image-20221230193405256" src="https://user-images.githubusercontent.com/7532477/210070644-e868f67b-0392-4bff-8760-4a550d809b9b.png">


# 使用

###  配置

根据需要修改config.conf

默认config.conf

```python
[fofa]
email:admin@fofa.so
api_key:813f62cdea45b4e00fbc0b1b6745d0dc

[scan_rule]
ports:80,443,8080,8081,7001,8088
portscan_timeout = 5
http_timeout = 8
http_code:200
path_deep = 3 

[dics_rule]
ext:zip,rar,tar.gz,7z,bz2,xz
date_year = 2010-2020

```



### 扫描备份文件

```bash
py -3 PointSearch.py -L urls.txt -t 50 -o res.txt
```

<img width="909" alt="poc1" src="https://user-images.githubusercontent.com/7532477/210070363-2b186a2b-b452-4791-aea9-e14e4a4f591a.png">


![image-20221230193731755](https://user-images.githubusercontent.com/7532477/210070695-9cf3e688-ac68-42a4-85ca-92633268c057.png)

### Rad爬虫递归扫描

关于rad爬虫配置使用请参考官方文档

https://github.com/chaitin/rad

```bash
# 爬取url
py -3 rad_windows_amd64\rad_spider_mul.py -u http://test.com/test -p rad_windows_amd64\rad_windows_amd64.exe
# 从json文件提取url文件
py -3 rad_windows_amd64\json_dump_data.py -m 2 -f parse_out\
# 扫描urls
py -3 PointSearch.py -l http://test.com -a 4
```



对于单个目标爬取的结果，可以直接通过json_dump_data.py -k URL 参数提取到文件通过-L参数进行扫描。

### 扫描敏感文件

关于敏感文件的扫描，仅仅使用了请求响应码来判断，建议使用dirsearch等扫描工具扫描，如果执意要使用本功能，建议checkwaf后再扫描，结果可使用以下命令统计筛选

```bash
cat log.txt |cut -d "/" -f 3 | sort | uniq -c
```
![image-20221230201645485](https://user-images.githubusercontent.com/7532477/210070803-6de0bac2-12d9-4f1b-8e29-97020eedde0a.png)

字典目录说明：

dirs：存放要扫描的目录，递归扫描的使用会用到此目录里面的路径

file: 存放要扫描的备份文件

filenames:存放要扫描的文件，不包含后缀，使用config.conf配置的后缀结合形成字典

sensive: 存放springboot\.git\等敏感文件

扫描目录的时候会把以上字典文件结合去重之后进行全部扫描

