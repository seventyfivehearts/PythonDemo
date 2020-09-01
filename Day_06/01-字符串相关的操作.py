# # 修改大小写
# print('hello'.capitalize())
# # upper 全大写
# print('hello'.upper())
# # lower 全小写
# print('hello'.lower())
# # title 每个单词的首字母大写
# print('hello'.title())
# while True:
#     content = input('请输入内容，输入exit退出')
#     print('输入的内容是', content)
#     # 不区分大小写
#     # 通过lower把大写转为小写来判断，不论输入的字符是什么
#     if content.lower() == 'exit':
#         break

# ljust(width,fillchar) rjust center
# width长度 fillchar 填充字符，默认使用空格
# 让字符串以指定长度显示，如果长度不够，用空格补齐，默认在右边
# 超过了，输入什么打印什么
# print('Monday'.ljust(10, '-'))
# print('Monday'.rjust(12, '-'))

# print('apple'.center(20, '='))

# lstrip 去除掉左边的空格
print('    apple   '.lstrip())
# rstrip 去掉右边的空格
print('    apple   '.rstrip())
# strip 去掉空格
print('    apple   '.strip())


# 字符串的运算符
#  + 拼接字符串
# 字符串和数字之间是用乘法运算
# 字符串和数字之间做==运算
# 字符串之间比较运算，会逐个比较字符串的编码
# 不支持其他运算

