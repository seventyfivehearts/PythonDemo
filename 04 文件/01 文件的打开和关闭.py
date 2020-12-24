# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 19:29
# @Author  : sunzhen
# @File    : 01 文件的打开和关闭.py
# @Software: PyCharm

# 使用 open() 内置函数打开文件
# 参数如下：
# file:	指定文件打开的路径
# mode: 文件打开的模式，默认使'r'只读
# encoding: 文件打开的编码格式
# open(file, mode='r', buffering=None
# encoding=None, errors=None
# newline=None, closefd=True
f = open('xxx.txt', mode='r', encoding='utf-8')

# <_io.TextIOWrapper name='xxx.txt' mode='r' encoding='utf-8'>
print(f)
# 读的和写的一样的才能不出问题
# windows操作系统里面打开文件的编码格式 默认使 gbk格式
print(f.read())

# 需要保持一个打开文件要关闭的习惯
# 关闭文件
f.close()
