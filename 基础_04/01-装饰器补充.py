# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 15:10
# @Author  : sunzhen
# @File    : 笔记-装饰器补充.py
# @Software: PyCharm

# 将原函数的属性赋值给wrapper
from functools import wraps

def outter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    # 手动 将原函数的属性赋值给wrapper
    # index.__name__ = 原函数.__name__
    # index.__doc__ = 原函数.__doc__
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper

@outter
def index(x, y):
    """这个是主页功能"""
    print(x, y)


index(1, 2)
# 偷梁换柱,即原函数名指向的内存地址偷梁换柱
# 所以应该将wrapper做的和原函数一样


print(index.__name__)  # <function index at 0x000002716B3C0280>
print(help(index))  # 加了注释器之后看的文档注释是wrapper的注释


