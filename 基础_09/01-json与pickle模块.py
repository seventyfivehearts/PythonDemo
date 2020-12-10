# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 11:20
# @Author  : sunzhen
# @File    : 笔记-json与pickle模块.py
# @Software: PyCharm

#  1.什么是序列化
#  序列化指的是把内存的数据类型转换成一个特定的格式的内容
#  该格式的内容可用于存储或者传输给其他平台使用
#  内存中的数据类型----->序列化----->特定的格式(json格式或者pickle格式)
#  内存中的数据类型<-----序列化<-----特定的格式(json格式或者pickle格式)

# 2.为何要序列化
# 序列化得到两个特殊的格式:
# 1.可用于存储 -->用于存档
# 2.传输给其他平台-->跨平台数据交互
# python                              java
#    列表         特定格式                  数组

# 针对用途一：应该是一种通用，能够被所有语言识别的格式 pickle只有python可以识别
# 针对用途二：应该是一种通用，能够被所有语言识别的格式 json


# 3.如何序列化与反序列化

# json验证: json格式兼容的是所有语言通用的数据类型,不能识别某一语言的特有类型
import json

# json.dumps({1,2,3}) # Object of type set is not JSON serializable

# json强调 单引号
# l = json.loads('[1,1.3,"aaa",true,false]')
# print(l[0]) # 1

# 猴子补丁
# 应该在入口处的地方打补丁 如start.py
# import ujson

# json.dumps() = 更好的功能
# json.loads() = 更好的功能
# def monkey_patch_json():
#     json.__name__ = 'ujson'
#     json.dumps = ujson.dumps
#     json.loads = ujson.loads

# 5.pickle

# 6.xml模块
# 7.






















