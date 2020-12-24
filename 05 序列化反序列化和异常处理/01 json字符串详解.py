# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 9:05
# @Author  : sunzhen
# @File    : 01 json字符串详解.py
# @Software: PyCharm

# 序列化: 将数据持久化保存的过程
# 反序列化: 将数据从硬盘写入内存
file = open('names.txt', 'w',encoding='utf-8')
file.write('张三')
file.close()