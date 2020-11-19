# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 14:39
# @Author  : sunzhen
# @File    : 03-模块搜索路径的优先级.py
# @Software: PyCharm

# 模块的查找的优先级
# 优先级
# 1.内存(内置模块)
# 2.从硬盘找 sys.path,按照他的路径去找
#   第一个文件夹是当前文件执行的文件夹,值为一个列表
# import sys
#
# print(sys.path)

# sys.modules 可以查看已加载在内存中的模块
import sys

print(sys.modules)


