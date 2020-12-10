# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 16:06
# @Author  : sunzhen
# @File    : 笔记.py
# @Software: PyCharm

"""
1.叠加多个装饰器的加载，运行分析(了解)(***)
# @deco1 # index=deco1(deco2.wrapper的内存地址)
# deco2  # deco2.wrapper的内存地址=deco2(deco3.wrapper的内存地址)
# deco3  # deco3.wrapper的内存地址=deco3(index)
# def index():
#     pass
"""
def func():
    pass

# 生成器的高级用法   yield挂起函数：yield的表达式形式(****)
#       yield 返回值 (默认返回none)

# 三元表达式
# 生成式
#     列表生成式
#     字典生成式
#     生成器生成式

# 函数的递归调用
# 二分法
