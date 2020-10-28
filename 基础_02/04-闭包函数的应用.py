# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 8:41
# @Author  : sunzhen
# @File    : 04-闭包函数的应用.py
# @Software: PyCharm
import requests


def outter(url):
    # url = 'https://www.baidu.com' # 把这个url当成参数传进去
    def get():
        response = requests.get(url)
        print(len(response.text))

    return get


f = outter('https://www.baidu.com')
f()
# 传参的方案一
# get('https://www.baidu.com')
# get('https://www.cnblogs.com/linhaifeng')

# 第二种方式 使用闭包
