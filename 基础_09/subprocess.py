# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 17:49
# @Author  : sunzhen
# @File    : subprocess.py
# @Software: PyCharm
import subprocess

'''
sh-3.2# ls /Users/egon/Desktop |grep txt$
mysql.txt
tt.txt
事物.txt
'''

res1 = subprocess.Popen('mkdir /Users/Desktop', shell=True, stdout=subprocess.PIPE)
res = subprocess.Popen('grep txt$', shell=True, stdin=res1.stdout,
                       stdout=subprocess.PIPE)

print(res.stdout.read().decode('utf-8'))

# 等同于上面,但是上面的优势在于,一个数据流可以和另外一个数据流交互,可以通过爬虫得到结果然后交给grep
res1 = subprocess.Popen('ls /Users/jieli/Desktop |grep txt$', shell=True, stdout=subprocess.PIPE)
print(res1.stdout.read().decode('utf-8'))

# windows下:
# dir | findstr 'test*'
# dir | findstr 'txt$'
import subprocess

res1 = subprocess.Popen(r'dir C:\Users\Administrator\PycharmProjects\test\函数备课', shell=True, stdout=subprocess.PIPE)
res = subprocess.Popen('findstr test*', shell=True, stdin=res1.stdout,
                       stdout=subprocess.PIPE)

print(res.stdout.read().decode('gbk'))  # subprocess使用当前系统默认编码，得到结果为bytes类型，在windows下需要用gbk解码
