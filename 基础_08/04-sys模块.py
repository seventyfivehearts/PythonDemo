# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 15:10
# @Author  : sunzhen
# @File    : 04-sys模块.py
# @Software: PyCharm
# 打印进度条
# [#    ]
# [##   ]
# [###  ]
# [###  ]

import time
recv_size = 0
total_size = 333333


def progress(percent):
    if percent > 1:
        percent = 1
    res = int(50 * percent) * '#'
    print('\r[%-50s]%d%%' % (res, int(100 * percent)), end='')


while recv_size < total_size:
    time.sleep(0.1)
    recv_size += 1024
    percent = recv_size / total_size

    progress(percent)
