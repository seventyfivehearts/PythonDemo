# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 11:45
# @Author  : sunzhen
# @File    : 03-os模块.py
# @Software: PyCharm
import os

print(os.path.abspath(__file__))

res = os.path.split('/a/a/a/a.txt')
print(res)
print(os.path.basename(r'/a/a//a'))