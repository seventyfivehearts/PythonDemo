# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 15:44
# @Author  : sunzhen
# @File    : index.py
# @Software: PyCharm
import mod
import student_manager
import tools
import file_manager


def login():
	data = file_manager.read_json('data.json', {})
	teacher_name = input('请输入账号(3-6位)：')
	if teacher_name not in data:
		print('账号不存在，请重新输入！')
		return
	
	password = input('请输入密码：')
	if data[teacher_name] == tools.encrypt_password(password):
		print('密码正确，登录成功')
		student_manager.name = teacher_name
		student_manager.show_manager()
	else:
		print('密码错误，登录失败！')


def register():
	data = file_manager.read_json('data.json', {})
	while True:
		teacher_name = input('请输入账号(3-6位)')
		if not 3 <= len(teacher_name) <= 6:
			print('输入有误请重新输入')
		else:
			break
	
	if teacher_name in data:
		print('用户存在,请重新输入')
		return
	
	while True:
		password = input('请输入密码(6-12位)')
		if not 3 <= len(password) <= 6:
			print('输入有误请重新输入')
		else:
			break
	# teacher[teacher_name] = password
	# # 把数据写进去
	# file_manager.write_json('data.json', teacher)
	t = mod.Teacher(teacher_name, password)
	# 密码加密
	data[t.name] = t.password
	file_manager.write_json('data.json', data)


# print(data)


def start():
	content = file_manager.read_file('welcome.txt')
	while True:
		option = input(content + '\n请输入你的操作(1-3):')
		if option == '1':
			login()
		elif option == '2':
			register()
		elif option == '3':
			break
		else:
			print('你输入的有误\n')


if __name__ == '__main__':
	start()
