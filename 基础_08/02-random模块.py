# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 11:23
# @Author  : sunzhen
# @File    : 02-random模块.py
# @Software: PyCharm
# import random
# (0,1) --float 大于0且小于1之间的浮点数
# print(random.random())


#  应用 随机验证码

import random

res = ''
for i in range(6):
    s1 = chr(random.randint(65, 90))
    s2 = str(random.randint(0, 9))
    res += random.choice([s1, s2])

print(res)
