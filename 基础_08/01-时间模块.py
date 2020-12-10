# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 16:06
# @Author  : sunzhen
# @File    : 笔记-时间模块.py
# @Software: PyCharm

# time 模块
import time
# 时间分为三种格式：
# 1.时间戳 从1970年到现在
# print(time.time())
# 作用 用于时间间隔的计算

# 2.按照某种格式显示的时间：2020-11-22 11:11:11
# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
# print(time.strftime('%Y-%m-%d %X %p'))
# 作用：用于展示时间

# 3.结构化时间
# 作用：用于单独获取时间的某一部分
# res = time.localtime()
# print(res)
# print(res.tm_mday)
# print(res.tm_year)


# datatime 模块
# import datetime
# 1.获取当前时间 datetime.datetime.now()
# print(datetime.datetime.now())
# print(datetime.datetime.now() + datetime.timedelta(days=2))


# 时间模块需要掌握的操作
# 1.时间格式的转化
import time

# 结构化时间转为时间戳 time.mktime()
s_time = time.localtime()
# print(time.mktime(s_time))
#  时间戳转为结构化时间
# tp_time = time.time()
# print(time.localtime(tp_time))

# print(time.gmtime())  # 世界标准时间

# 需要掌握的 format string ---> timestamp

# 1988-笔记-笔记 11:11:11  + 7天

# 1.先把格式化字符串时间转为结构化时间

# struct_time = time.strptime('1988-笔记-笔记 11:11:11',
#                             '%Y-%m-%d %H:%M:%S')
# 2.在把结构化时间转为时间戳
# timestamp = time.mktime(struct_time) + 7*24*60*60

# 3.最后把时间戳转为格式化时间
# res = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))
# print(res)
time.sleep(3)
# 了解













