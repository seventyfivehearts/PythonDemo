# -*- coding: utf-8 -*-
# @Time    : 2021/1/1 10:23
# @Author  : sunzhen
# @File    : student_manager.py
# @Software: PyCharm
import file_manager
import mod


def add_student():
	while True:
		# students = []
		x = file_manager.read_json(name + '.json', {})
		if not x:
			students = []
			num = 0
		else:
			students = x['all_student']
			num = int(x['num'])
		
		s_name = input('输入姓名：')
		s_age = input('输入年龄：')
		s_gender = input('输入性别：')
		s_tel = input('输入电话号')
		
		num += 1
		s_id = 'stu_' + str(num).zfill(4)
		
		s = mod.Student(s_id, s_name, s_age, s_gender, s_tel)
		students.append(s.__dict__)
		data = {'all_student': students, 'num': len(students)}
		file_manager.write_json(name + '.json', data)
		choice = input('添加成功！\n1继续\n2返回\n请选择(1-2):')
		if choice == '2':
			break


def show_student():
	choice = input('1查看所有学生\n2根据姓名查找学生\n3根据学号查找学生\n其他：返回\n选择：')
	# 读文件
	data = file_manager.read_json(name + '.json', {})
	students = data.get('all_student', [])
	
	if not students:
		print('未添加学员，请重新添加')
		return
	if choice == '1':
		pass
	elif choice == '2':
		s_name = input('请输入姓名：')
		students = filter(lambda s: s['name'] == s_name, students)
	elif choice == '3':
		s_id = input('请输入ID：')
		students = filter(lambda s: s['s_id'] == s_id, students)
	else:
		print('输入有误！')
		return
	for student in students:
		print('学号: {s_id}, 姓名：{name}, 年龄：{age}, 性别：{gender}, ☎：{tel}'.format(**student))


def change_student():
	pass


def delete_student():
	data = file_manager.read_json(name + '.json', {})
	students = data.get('all_student', [])
	key = value = ''
	if not students:
		print('文件未找到')
		return
	num = input('1.按姓名删\n2.按ID删\n3.其他返回')
	if num == '1':
		key = 'name'
		value = input('输入要删除的姓名：')
	elif num == '2':
		key = 's_id'
		value = input('输入要删除的id:')
	else:
		return
	
	student = filter(lambda s: s.get(key, '') == value, students)
	for i, s in enumerate(student):
		print('{x} 学号:{s_id}, 姓名:{name},性别:{gender},年龄:{age}, ☎:{tel}'.format(x=i, **s))
	n = input('请输入需要删除的学生的标号(0~{}),q-返回:'.format(i))  # 使用变量 i 有潜在风险
	
	if not n.isdigit() or not 0 <= int(n) <= i:
		print('输入的内容不合法')
		return
	
	# 将学生从all_students里删除
	students.remove(students[int(n)])
	
	data['all_student'] = students
	file_manager.write_json(name + '.json', data)


name = ''


def show_manager():
	content = file_manager.read_file('students_page.txt') % name
	while True:
		print(content)
		option = input('请输入1-5：')
		if option == '1':
			add_student()
		elif option == '2':
			show_student()
		elif option == '3':
			change_student()
		elif option == '4':
			delete_student()
		elif option == '5':
			break
		else:
			print('输入有误！')
