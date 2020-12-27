# -*- coding: utf-8 -*-
# @Time    : 2020/12/27 17:04
# @Author  : sunzhen
# @File    : card.py
# @Software: PyCharm
user_dict = [
	{'name': '张三', 'tel': 123456789, 'qq': 123},
	{'name': '李四', 'tel': 987654321, 'qq': 123},
	{'name': '周六', 'tel': 213143454, 'qq': 345}
]


def add_user():
	name = input('请输入你的名字：')
	for user in user_dict:
		if user['name'] == name:
			print('你输入的名字存在，请重新输入')
			break
		else:
			tel = input('请输入你的电话：')
			qq = input('请输入你的qq：')
			user = {'name': name, 'tel': tel, 'qq': qq}
			user_dict.append(user)


# print(user_dict)


def check_numbers(del_user_num):
	if del_user_num.isdigit():
		num = int(del_user_num)
		if 0 < num < len(user_dict):
			return True
		else:
			return False


def delete_user():
	del_user_num = input('请输入你要删除的序号(序号从0开始)：')
	is_value = check_numbers(del_user_num)
	if is_value:
		answer = input('你确定要删除 yes/no')
		if answer == 'yes':
			user_dict.pop(int(del_user_num))
	else:
		print('你输入的不正确')
	print(user_dict)


def change_user():
	change_user_num = input('请输入你要修改的序号(序号从0开始)：')
	if check_numbers(change_user_num):
		user = user_dict[int(change_user_num)]
		# print('你要修改的信息是{name}, {tel}, {qq}'.format(**user))
		new_name = input('请输入新的姓名:')
		for u in user_dict:
			if u['name'] == new_name:
				print('新用户名已经存在')
				change_user()
				return
		else:
			new_tel = input('请输入新的手机号:')
			new_qq = input('请输入新的QQ号:')
			if new_name == user['name'] and new_tel == user['tel'] and new_qq == user['qq']:
				print('信息未修改')
			else:
				user['name'] = new_name
				user['tel'] = new_tel
				user['qq'] = new_qq


def query_user():
	search_name = input('请输入要查询的姓名:')
	for user in user_dict:
		if user['name'] == search_name:
			print('查询到的信息如下:\n姓名:{name},手机:{tel},QQ:{qq}'.format(**user))
			break
	else:
		print('没有您要找的信息....')


def show_all():
	print('序号  姓名  手机号  QQ')
	for i, u in enumerate(user_dict):
		print(i, u['name'], u['tel'], u['qq'])


def exit_card():
	answer = input('是否要退出？yes/no')
	return answer.lower() == 'yes'


def start():
	while True:
		print('-------名片管理系统-------\n 1添加名片\n 2删除名片\n 3修改名片\n 4查询名片\n 5展示所有名片\n 6退出系统')
		option = input('请输入你想要的操作(数字)：')
		if option == '1':
			add_user()
		elif option == '2':
			delete_user()
		elif option == '3':
			change_user()
		elif option == '4':
			query_user()
		elif option == '5':
			show_all()
		elif option == '6':
			is_exit = exit_card()
			if is_exit:
				break
		else:
			print('你输入的不正确，请重新输入')


if __name__ == '__main__':
	start()
