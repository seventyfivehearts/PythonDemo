# -*- coding: utf-8 -*-
# @Time    : 2020/10/23 20:20
# @Author  : sunzhen
# @File    : 01-函数对象.py
# @Software: PyCharm
'''
1.函数对象
2.函数嵌套
3.闭包函数 = 名称空间与作用域+函数嵌套+函数对象
    核心点：名字的查找关系是以函数定义阶段为准的

'''


# 精髓 可以把函数当成变量去用
# func = 内存地址
def func():
    print('from func')


# 1.可以赋值
# f = func
# print(f,func)
# f()

# 2.当作含函数的参数传给另一个函数
# def foo(x):  # x = func的内存地址
#     # print(x)
#     x()
#
#
# foo(func)  # foo(func的内存地址)

# 3.可以当作函数  可以当作另一个函数的返回值
# def foo(x):  # x = func的内存地址
#     return x
# res = foo(func)
# print(res)
#
# res() # 当作函数 然后调用

# 当作容器类型的元素

# # 列表
# l = [func,]
# print(l)
# l[0]()

# 字典
# dic = {'k1':func}
# print(dic)
# dic['k1']() # 内存地址加括号调用函数

# 示例
def login():
    print('登录功能')


def transfer():
    print('转账功能')


def get_money():
    print('查询余额')


# 用字典的形式
func_dict = {
    '0': ['退出', None],
    '1': ['登录', login],
    '2': ['转账', transfer],
    '3': ['查询余额', get_money]
}

while True:
    # print("""
    # 0 退出
    # 1 登录
    # 2 转账
    # 3 查询余额
    # """)

    for k in func_dict:
        print(k, func_dict[k][0])

    choice = input('请输入命令编号：').strip()  # 去掉空格
    if choice == '0':
        break

    if choice in func_dict:
        func_dict[choice][1]()
    else:
        print('输入的代码不正确')
    # 优化 使用函数的内存地址
    # if not choice.isdigit():
    #     continue
    # if choice == '0':
    #     break
    # if choice == '1':
    #     login()
    # elif choice == '2':
    #     transfer()
    # elif choice == '3':
    #     get_money()
    # else:
    #     print('输入的代码不正确')
