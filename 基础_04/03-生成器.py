# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 17:31
# @Author  : sunzhen
# @File    : 03-生成器.py
# @Software: PyCharm
#   自定义迭代器

# 如何得到自定义的迭代器
# 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码
# 会返回一个生成器对象,生成器即自定义的迭代器

def func():
    print('第一次')
    yield 1 # 能返回多次值
    print('第二次')
    yield 2


g = func()
print(g)  # <generator object func at 0x000001B7168C63C0>(生成器)
# 生成器就是迭代器
# g.__iter__()
# g.__next__()

# 会触发函数体代码的运行,然后遇到yield停下来,将yield后的值当作本次调用的结果返回

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__()) # StopIteration(会超出范围)





























