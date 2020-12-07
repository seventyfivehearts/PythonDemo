# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 12:08
# @Author  : sunzhen
# @File    : 02-实现面向对象编程.py
# @Software: PyCharm

# 一、先定义类(推荐使用驼峰体)
#   类是对象类似于数据与功能的集合体
#   类当中通常包含的是变量和函数，但是类当中其实可以写任意其他代码
#   注意: 类体代码是在定义阶段就会立即执行，会产生类的名称空间

class Students:
    # 1)变量的定义
    stu_schools = 'world'

    # 2)功能的定义
    def set_info(stu_obj, x, y, z):
        stu_obj['stu_name'] = x
        stu_obj['stu_age'] = y
        stu_obj['stu_gender'] = z

    # print('====>')


# Students.__dict__ 下面存放的字典
# print(Students.__dict__)
# print(Students.__dict__['set_info'])


# 类专门的取值的语法
# 属性访问的语法
# 1)访问数据属性
# print(Students.stu_schools)  # 本质上是 Students.__dict__['set_info']
# 2)访问函数属性
# print(Students.set_info)
# 添加  本质上是操作字典
# Students.x = 111  # Students.__dict__['x'] = 111


# 二、调用类产生对象
# 对象

# stu1_obj = Students()
# stu2_obj = Students()
# stu3_obj = Students()
# 底层是在操作字典


# 代码重复
# 属性的查找顺序
# stu1_obj.stu_name = 'carter'  # stu1_obj.__dict__['stu_name'] = 'carter'
# stu1_obj.stu_age = 18  # stu1_obj.__dict__['stu_age'] = 18
# stu1_obj.stu_gender = 'male'  # stu1_obj.__dict__['stu_gender']  = 'male'
# print(stu1_obj.__dict__)

# stu2_obj.stu_name = 'carter'  # stu1_obj.__dict__['stu_name'] = 'carter'
# stu2_obj.stu_age = 18  # stu1_obj.__dict__['stu_age'] = 18
# stu2_obj.stu_gender = 'male'  # stu1_obj.__dict__['stu_gender']  = 'male'
# print(stu2_obj.__dict__)

# stu3_obj.stu_name = 'carter'  # stu1_obj.__dict__['stu_name'] = 'carter'
# stu3_obj.stu_age = 18  # stu1_obj.__dict__['stu_age'] = 18
# stu3_obj.stu_gender = 'male'  # stu1_obj.__dict__['stu_gender']  = 'male'
# print(stu3_obj.__dict__)

# 解决代码重复问题 使用函数

# 方案一
# def init(obj, x, y, z):
#     obj.stu_name = x
#     obj.stu_age = y
#     obj.stu_gender = z
#
#
# init(stu1_obj, 'carter', 18, 'male')
# init(stu2_obj, 'jack', 20, 'male')
# init(stu3_obj, 'mary', 21, 'female')

# 方案二
# 先定义类
class Student:
    # 1)变量的定义
    stu_schools = 'world'

    # 在类调用阶段运行
    # 空对象，('carter', 18, 'male')
    def __init__(obj, x, y, z):
        obj.stu_name = x    # 空对象.stu_name = 'carter'
        obj.stu_age = y     # 空对象.stu_age = 18
        obj.stu_gender = z  # 空对象.stu_gender = 'male'

    # 2)功能的定义
    def set_info(stu_obj, x, y, z):
        stu_obj['stu_name'] = x
        stu_obj['stu_age'] = y
        stu_obj['stu_gender'] = z

    # print('====>')


# 二 再调用类产生对象

# 调用类的过程又称之为实例化
# 1.先产生一个空对象
# 2，python会自动调用类中的__init__方法
#   将空对象已经调用类是括号传入的参数传入给__init__方法
# 3.返回初始化完的对象
stu1_obj = Student('carter', 18, 'male')
stu2_obj = Student('jack', 20, 'male')
stu3_obj = Student('mary', 21, 'female')
print(stu1_obj.__dict__)


# 总结 __init__方法
# 1.会在调用类时自动触发执行，用来为对象初始化自己独有的数据
# 2.__init__应该存放对象初始化属性的功能，但是也是可以存放其他的
#   代码的，可以存放想要在类调用时立刻执行的代码
# 3.init方法返回None






















