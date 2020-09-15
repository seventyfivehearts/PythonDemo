person = {'name': '张三',
          'age': '18',
          'height': '180',
          'weight': '100',
          'isPass': True,  # o可以是布尔值
          'hobbies': ['play', 'eat', 'etc']  # 可以对应多个 ,列表
          }
# 修改  使用 key 来修改,可以设置默认值
# 存在,修改对应的值,不存在会在字典中新添加一个key-value


person['name'] = '李四'
person['gender'] = 'female'
print(person)

