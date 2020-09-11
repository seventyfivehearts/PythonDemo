person = {'name': '张三',
          'age': '18',
          'height': '180',
          'weight': '100',
          'isPass': True,  # o可以是布尔值
          'hobbies': ['play', 'eat', 'etc']  # 可以对应多个 ,列表
          }
# 字典里的key 是不允许重复的, 重复的话是不会报错的,后一个key会覆盖前一个
# 字典中的value可以是任意类型的数据 ,但是 key 必须是不可变数据类型, 一般使用字符串
print(person)
