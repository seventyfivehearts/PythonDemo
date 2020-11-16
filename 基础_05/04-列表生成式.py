# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 16:04
# @Author  : sunzhen
# @File    : 04-列表生成式.py
# @Software: PyCharm

# 列表生成式
a = ['a_a', 'b_a', 'c']
# 把后缀是_a的元素提取到一个新的列表里面去

# b = []
# for name in a:
#     if name.endswith('_a'):
#         b.append(name)

# print(b)


# 列表表达式将上面列表写的更精简一些

# [expression for item1 in iterable if condition1]
#
# b = [name for name in a if name.endswith('_a')]
# # 如果不加条件,判断永远为真
# # [name for name in a]
# print(b)
# # 把小写字母换成大写字母
# res = [name.upper() for name in a]
# print(res)
# # 把_a后缀去掉
# res = [name.replace('_a', '') for name in a]
# print(res)

# 其他生成式

# 字典生成式
# key = ['name', 'name1', 'name2']
#
# dic = {key: None for key in key}
# print(dic)


# items = [('name', 'sunzhen'), ('age', 18)]
# res = {k: v for k, v in items if k != 'age'}
#
# print(res)

# 集合生成式(只要单独的一个值)
# keys = ['name', 'age', 'gender']
# set1 = {key for key in keys}
# print(set1)

with open('01.py', mode='rt', encoding='utf-8') as f:
    # 方式一
    # for line in f:
    #     res = 0
    #     res += len(line)
    # print(res)
    # 方式二
    # size_of_line = [len(line) for line in f]
    res = sum([len(line) for line in f])
    print(res)
    # 方式三   效率最高
    res = sum(len(line) for line in f)



