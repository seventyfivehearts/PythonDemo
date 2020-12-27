# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 9:05
# @Author  : sunzhen
# @File    : 01 json字符串详解.py
# @Software: PyCharm

# 序列化: 将数据持久化保存的过程
# 反序列化: 将数据从硬盘写入内存
names = ['张三', '李四']
file = open('names.txt', 'w', encoding='utf-8')
# write 只能写入字符串或者二进制
# 将数据转换为字符串
# 	可以使用json 将数据写入 (本质是字符串)
# 将数据准换为二进制
file.write('张三')

# json持久存储化有两个方法 dumps dump
# 1.dumps 将数据转为json字符串，不保存数据在文件中
# 2.dump 将数据转为json字符串，保存数据在文件中

import json
json.dump(names, file)
file.close()

# json反序列化 loads load
# loads 将json数据加载成为Python数据中
# load	读文件，把文件中的数据加载到Python数据中

# pickle模块