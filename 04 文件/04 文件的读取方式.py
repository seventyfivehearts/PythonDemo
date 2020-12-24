# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 19:30
# @Author  : sunzhen
# @File    : 04 文件的读取方式.py
# @Software: PyCharm

# open 默认以'rt' 只读文本形式打开的
file = open('xxx.txt', encoding='utf-8')
# print(file.read())  # 将所有数据都读出来
# print(file.readline()) 	# 只读取一行数据

print(file.readlines())  # 将数据读出到一个元组里
file.close()
