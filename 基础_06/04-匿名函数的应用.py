# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 10:24
# @Author  : sunzhen
# @File    : 04-匿名函数的应用.py
# @Software: PyCharm


salaries = {
    'name1': 2000,
    'name2': 2300,
    'name3': 2600,
    'name4': 2900,
    'name5': 3000
}

# 需求1:找到薪资最高的那个人

# def func(k):
#     return salaries[k]
#
#
# # res = max(salaries,key=func)
# # 因为函数只使用一次,可以使用lambda
# res = max(salaries, key=lambda k: salaries[k])
#
# print(res)
#
#
# res = min(salaries,key= lambda k:salaries[k])
# print(res)

salaries = {
    'name1': 2000,
    'name2': 2300,
    'name3': 2600,
    'name4': 2900,
    'name5': 3000
}
# sorted 排序的应用
# sorted(reverse=True) 从大到小排序的
# res = sorted(salaries, key=lambda k: salaries[k])
# print(res)

# map
# l = ['name1', 'name2', 'name3']
# 第一种
# new_l = [name + '_sss' for name in l]
# print(new_l)
# 第二种
# res = map(lambda name: name + '_sss', l)
# print(res)

# filter
l = ['name1_ss', 'name2_ss', 'name3']

# reduce
