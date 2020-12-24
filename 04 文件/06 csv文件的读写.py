# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 19:31
# @Author  : sunzhen
# @File    : 06 csv文件的读写.py
# @Software: PyCharm

import csv

file = open('demo.csv', 'w', encoding='utf-8', newline='')
w = csv.writer(file)
w.writerow(['name', 'age', 'score'])
w.writerow(['张三', '19', '100'])
w.writerow(['李四', '20', '99'])
w.writerow(['王五', '21', '80'])
file.close()
