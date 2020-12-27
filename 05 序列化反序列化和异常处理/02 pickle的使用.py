# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 9:06
# @Author  : sunzhen
# @File    : 02 pickle的使用.py
# @Software: PyCharm

# Python存入数据只支持 字符串和二进制
# json(将str/list/tuple/dict)转换为相应的数据类型
# pickle将任一数据转为二进制

import pickle

# 序列化 dumps 把Python中的数据加载成为二进制
# dump 把Python中的数据加载为二进制并保存到文件中
# 反序列化 loads 把二进制数据转为Python数据
# 			load 把文件中的二进制数据转为Python对象

names = ['张三', '李四', '王五']
# d_name = pickle.dumps(names)  # b'\x80\x04\x95 \x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x06\xe5\xbc
# # \xa0\xe4\xb8\x89\x94\x8c\x06\xe6\x9d\x8e\xe5\x9b\x9b\x94\x8c\
# # x06\xe7\x8e\x8b\xe4\xba\x94\x94e.'
#
# print(d_name)
#
# file = open('names.txt', 'wb')
# file.write(d_name)
# file.close()
#
# # 反序列化
# file1 = open('names.txt', 'rb')
# a = file1.read()
# print(pickle.loads(a))  # ['张三', '李四', '王五']
#
# file1.close()

file = open('names.txt', 'wb')
pickle.dump(names, file)
file.close()

file2 = open('names.txt', 'rb')
pickle.load(file2)
file2.close()
