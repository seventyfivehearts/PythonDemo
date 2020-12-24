# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 19:29
# @Author  : sunzhen
# @File    : 02 路径的介绍.py
# @Software: PyCharm

# 使用 open() 内置函数打开文件
# 参数如下：
# file:	指定文件打开的路径
# mode: 文件打开的模式，默认使'r'只读
# encoding: 文件打开的编码格式

# 绝对路径 从电脑盘符开始的路径
import os

# 在非windows 中开发使用 / 开发
print(os.sep)
# 路径的三种方式 1.\\  2.r'' 3./ (推荐)
# file = open('D:\\PycharmDemo\Demo\04 文件\\xxx.txt', encoding='utf-8')
# file = open(r'D:\PycharmDemo\Demo\04 文件\xxx.txt', encoding='utf-8')
file = open('D:/PycharmDemo/Demo/04 文件/xxx.txt', encoding='utf-8')
print(file.read())

# 相对路径: 当前文件所在的文件的路径
file = open('xxx.txt', encoding='utf-8')
# ../表示到上一级文件夹
# ./ 可以省略不写，表示当前文件夹
# / 不能胡乱使用
print(file.read())