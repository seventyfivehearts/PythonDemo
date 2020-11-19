# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 9:47
# @Author  : sunzhen
# @File    : 02-from...import导入模块的使用.py
# @Software: PyCharm

# import 导入模块在使用的时候必须加'模块.'
# 优点: 肯定不会与当前名称空间发生冲突
# 缺点: 显的很麻烦

# from...import 导入 发生三件事
# 1.产生一个模块的名称空间
# 2.运行模块文件将运行过程中产生的名字都丢到模块的名称空间中
# 3.在当前名称空间拿到一个名字,该名字与模块名称空间的某一个内存地址相同
# from model import x  # x -->指向模块model的内存地址
# from model import func
#
# print(x)
# print(func)
# func()


# from...import 导入模块在使用时不用加前缀
# 优点:代码更简洁
# 缺点:容易与当前名称空间混淆

# 一行导入多个名字(不推荐)

from model import *
# * 表示所有的都可以用(导入模块的所有)
# 不建议使用

# 起别名 (as)
from model import func as l





















