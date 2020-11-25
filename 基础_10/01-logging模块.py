# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 10:24
# @Author  : sunzhen
# @File    : 01-logging模块.py
# @Software: PyCharm
import logging

# logging.debug('debug')

# 一：日志配置
logging.basicConfig(
    # 1、日志输出位置：1、终端 2、文件
    filename='access.txt',   # 不指定，默认打印到终端

    # 2、日志格式
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',

    # 3、时间格式
    datefmt='%Y-%m-%d %H:%M:%S %p',

    # 4、日志级别
    # critical => 50
    # error => 40
    # warning => 30
    # info => 20
    # debug => 10
    level=10,
)

# 二：输出日志
logging.debug('调试debug')
logging.info('消息info')
logging.warning('警告warn')
logging.error('错误error')
logging.critical('严重critical')

'''
# 注意下面的root是默认的日志名字
WARNING:root:警告warn
ERROR:root:错误error
CRITICAL:root:严重critical
'''