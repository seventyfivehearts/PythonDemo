# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 17:14
# @Author  : sunzhen
# @File    : 03-属性查找.py
# @Software: PyCharm


class Student:
    # 1)变量的定义
    stu_schools = 'world'

    # 在类调用阶段运行
    # 空对象，('carter', 18, 'male')
    def __init__(self, x, y, z):
        self.stu_name = x  # 空对象.stu_name = 'carter'
        self.stu_age = y  # 空对象.stu_age = 18
        self.stu_gender = z  # 空对象.stu_gender = 'male'

    # 2)功能的定义
    def set_info(self, x, y, z):
        self.stu_name = x
        self.stu_age = y
        self.stu_gender = z
    def func(self):
        print('hello world')

    # print('====>')


stu1_obj = Student('carter', 18, 'male')
stu2_obj = Student('jack', 20, 'male')
stu3_obj = Student('mary', 21, 'female')
print(stu1_obj.__dict__)

# 类中存放的对象共有数据与功能的
# 一、类可以访问
#   1.类的数据属性 共享给所有数据
# print(Student.stu_schools)
#   2.类的函数属性
# print(Student.set_info)


# 二、类中的东西是给对象用的
# 1.类的数据属性是共享给所有对象用的，大家访问的地址都一样
# print(stu1_obj.stu_name)
# print(stu1_obj.stu_age)
# print(stu1_obj.stu_gender)
# print(stu1_obj.stu_schools)


# 2、类的函数属性是绑定给对象使用的
# 绑定方法的特殊之处在于：谁调用绑定方法就会将谁当作第一个参数自动传入

# print(Student.set_info)
# 严格按照函数的规则来用
# Student.set_info(stu1_obj, 'carter', 20, 'male')

# 绑定方法的特殊之处在于：谁调用绑定方法就会将谁当作第一个参数自动传入
# 其他严格按照函数的规则使用

# 在类中新定一个函数一定要传入一个参数用来接收绑定方法传入的参数 self
# stu1_obj.set_info('carter', 20, 'male')
# set_info(stu1_obj, 'carter', 20, 'male')



















