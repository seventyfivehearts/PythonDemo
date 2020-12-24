# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 19:29
# @Author  : sunzhen
# @File    : 03 文件的打开方式.py
# @Software: PyCharm

# r：只读模式，默认打开问价的方式，打开文件只读不写 如果文件不存在时会报错
# w：读写模式，打开文件只能写不能读，有文件则会覆盖这个文件，如果没有则创建这个文件
# b：rb rw 以二进制形式操作文件 可以用来操作非文本文件

file = open('xxx.txt', 'w')

file.write('hello')
# 如果文件不存在的时候会创建文件

