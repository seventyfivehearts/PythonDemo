# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 15:46
# @Author  : sunzhen
# @File    : 03-hashlib模块.py
# @Software: PyCharm

# 哈希的定义
#   hash是一类算法,该算法接受传入的内容,经过运算得到一串hash值
#   hash的特点:
#       1.只要传入的内容一样,得到的hash值必然一样
#       2.只要使用hash的算法不变,无论校验的内容有多大,得到的hash值长度都是固定的
#       3.不能通过hash值反解成内容

# hash的用途
#   1.特点2用于密码密文传输与验证
#   2.特点2,3用于文件完整性校验

# 如何用
# import hashlib
#
# m = hashlib.md5()
# m.update('hello'.encode('utf-8'))  # 必须是bytes类型
# m.update('world'.encode('utf-8'))  # 必须是bytes类型
# res = m.hexdigest()  # 得到'hello world'
# print(res)  # fc5e038d38a57032085441e7fe7010b0

# 例如
# m.update('文件的所有内容')
# m.hexdigest()
# 两个相同，推荐第二种方式，使用for循环
# 文件太大有弊端
# f = open('a.txt', mode='rb')
# f.seek()
# f.read(2000)
# m1 = hashlib.md5()
# m1.update('文件的一行')
# m1.update('文件的一行')
# m1.update('文件的一行')
# m1.update('文件的一行')
# m1.hexdigest()

import hashlib

passwds = [
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
]


def make_passwd_dic(passwds):
    dic = {}
    for passwd in passwds:
        m = hashlib.md5()
        m.update(passwd.encode('utf-8'))
        dic[passwd] = m.hexdigest()
    return dic


def break_code(cryp_tograph, passwd_dic):
    for k, v in passwd_dic.items():
        if v == cryp_tograph:
            print('密码是===>\033[46m%s\033[0m' % k)


cryp_tograph = 'aee949757a2e698417463d47acac93df'
break_code(cryp_tograph, make_passwd_dic(passwds))
