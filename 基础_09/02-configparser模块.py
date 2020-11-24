# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 15:14
# @Author  : sunzhen
# @File    : 02-configparser模块.py
# @Software: PyCharm

# 用来加载某种特定格式的配置文件
import configparser
# test.ini

config = configparser.ConfigParser()
config.read('test.ini')

# 1.获取所有的sections
print(config.sections())

# 2.获取某一section下的所有options(选择项)
print(config.options('section1'))

# 3.获取items
print(config.items('section1'))

# 4.获取某一个值
res = config.get('section1', 'user')
print(res)
# 获取到并转为int
res = config.getint('section1', 'age')
print(res)

config.getboolean('section1', 'is_admin')












