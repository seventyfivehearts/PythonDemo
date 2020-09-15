person = {'name': '张三',
          'age': '18',
          'height': '180',
          'weight': '100',
          'isPass': True,  # o可以是布尔值
          'hobbies': ['play', 'eat', 'etc']  # 可以对应多个 ,列表
          }

# 字典的遍历
# for in 循环 获取的是key
# # 可以通过key获取到value
# for i in person:
#     # print(i)
#     print(i, '=', person[i])
#
# # 通过获取到key ,然后通过key打印输出value
# print(person.keys())  # dict_keys(['name', 'age', 'height', 'weight', 'isPass', 'hobbies'])
# for k in person.keys():
#     print(k, '=', person[k])

# # 拿到value,但是过去不到key 基本不用
# print(person.values()) # dict_values(['张三', '18', '180', '100', True, ['play', 'eat', 'etc']])
# for i in person.values():
#     print(i)

# 使用 person.item()  item()中以键值对的形式存在
print(
    person.items())  # dict_items([('name', '张三'), ('age', '18'), ('height', '180'), ('weight', '100'), ('isPass', True), ('hobbies', ['play', 'eat', 'etc'])])

# for i in person.items():
#     print(i)
# 可以使用拆包的形式
for k, v in person.items():
    print(k, v)
