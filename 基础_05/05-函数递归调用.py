# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:58
# @Author  : sunzhen
# @File    : 05-函数递归调用.py
# @Software: PyCharm


# 函数的递归调用:是函数嵌套的一种特殊形式
# 具体指的是:
#       在调用函数的过程又直接调用到本身
# 递归的本质是循环

# 直接调用本身
# def f1():
#     # 最多调用1000次
#     print('笔记')
#     f1()
#
# f1()

# 间接调用本身
# def f2():
#     print('---->f2')
#     f1()
#
#
# def f1():
#     print('---->f1')
#     f2()
#
# f1()


# 需要注意的一点
# 递归调用不应该无限调用下去,必须满足某种条件之后停止掉
# def func(c):
#     if c == 10:
#         return
#     print(c)
#     c+=1
#     func(c)
# func(1)

# 递归的两个阶段
# 回溯:一层 一层调用下去
# 递推:满足某种结束条件,结束递归调用,然后一层一层返回


# 递归的应用
list1 = [1, [2, [3, [4, 5[6, 7]]]]]
def f1(list1):
    for i in list1:
        if type(list1):
            f1(list1)
        else:
            print(i)
f1(list1)
