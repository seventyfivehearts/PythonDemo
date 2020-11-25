# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 15:48
# @Author  : sunzhen
# @File    : src.py
# @Software: PyCharm

# 拿到日志的产生者 loggers


# 需要导入日志配置字典 LOGGING_DIC
import settings
# import logging.config
from logging import config,getLogger
config.dictConfig(settings.LOGGING_DIC)

log1 = getLogger('kkk')
log1.info('这是一条日志')

# 日志名的命名

# 日志轮转
#   日志记录着程序员运行过程中的关键信息 日志不能轻易删
#   新的日志不能一直累加在一个文件中
#
