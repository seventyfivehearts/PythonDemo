person = {'name': '张三',
          'age': '18',
          'height': '180',
          'weight': '100',
          'isPass': True,  # o可以是布尔值
          'hobbies': ['play', 'eat', 'etc']  # 可以对应多个 ,列表
          }
# pop用来删除键值对
person.pop('name')
print(person)
# popitem  删除键值对,可以返回删除的键值对的内容
print(person.popitem())

del person['age']
print(person)

person.clear()
print(person)
