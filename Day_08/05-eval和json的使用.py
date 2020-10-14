# 去重排序
nums = [1, 3, 4, 3, 4, 3, 5]
print(list(set(nums)))
# eval 可以执行字符串中的代码
# a = 'input("请输入用户名")'

# print(a)
# eval(a)
import json
# Json 把字典.列表,元组转换成为字符串
# 使用dumps 把字典,列表,元组转换为字符串
person = {"name": "张三", "age": 18, "gender": "feamale"}
n = json.dumps(person)
print(n)
# 不能像字典一样通过key获取到字符串
m = '{"name": "\u5f20\u4e09", "age": 18, "gender": "feamale"}'
s = json.loads(m)
# 把json字典转换为字符串
print(s)
print(type(s))
# Python        json
# True          true
# False         false
# 字符串           字符串
# 元组 列表         数组
# json数组转换回来的是列表



