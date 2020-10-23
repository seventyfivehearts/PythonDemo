# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 16:11
# @Author  : sunzhen
# @File    : 03 global与nonlobal.py
# @Software: PyCharm
# 示范1
# x = 111


# def fuc():
#     x = 222
#
#
# fuc()
# print(x)


# 示范2(如果在局部想要修改全局名字对应的值(不可变类型
# 使用global))
# x = 111
#
#
# def fuc():
#     global x # 声明名字时全局的名字,不需要在造新的名字了
#     x = 222


# fuc()
# print(x)


# 示例3
# a = [111, 222]
#
#
# def func():
#     a.append(333)
#
#
# func()
# print(a)

# nonlocal(了解) 修改函数外层函数包含的名字对应的值(不可变类型)

x = 0


def func():
    x = 1

    def fucn2():
        # 使用nonlocal (会逐层的找)
        nonlocal x

    fucn2()
    print('func内的x:', x)


func()
