# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 13:38
# @Author  : sunzhen
# @File    : 有参装饰器.py
# @Software: PyCharm

# # 无参装饰器模板
# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
#
#
# # 装饰器就是在不修改装饰对象源代码与调用方式的前提为其添加功能
# def index(x, y):
#     print(x, y)
#
#
# outer(index)
# index(1, 2)


# 一.知识储备
#
# def outer(func):
#     # func = 函数的内存地址
#     # wrapper参数不能动
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
#
#
# # 由于语法糖@的限制,outer只能有一个参数,并且该函数只是用来接收
# #                                  被装饰对象的内存地址
#
# @outer  # index=outer(index)  index=>wrapper
# def index(x, y):
#     print(x, y)
#
# # 偷梁换柱之后
# # index的参数什么样子,wrapper的参数就应该是什么样
# # from functools import wraps



# 第三层的参数是不受限制的,参数最多三层
# def outer(db_type,yy=11):
#
#     # db_type = file
#     def auth(func):
#         # func = 内存地址
#         def wrapper(*args, **kwargs):
#             name = input('your name>>:').strip()
#             pwd = input('your password>>:').strip()
#             if name == 'name' and pwd == '123':
#                 print('基于文件的验证')
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 print('账号错误')
#
#         return wrapper
#     return auth
#
# @outer
# def index(x, y):
#     print(x, y)
#
#
# index(1, 2)

# 有参装饰器的模板
def 有参装饰器(x,y,z):
    def outer(func):
        pass
@有参装饰器(1,2,3)
def 被装饰对象():
    pass












