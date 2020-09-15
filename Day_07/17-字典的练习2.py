person = [{'name': 'zhangsan', 'age': '18', 'height': 100},
          {'name': 'lisi', 'age': 19, 'height': 190},
          {'name': 'wangwu', 'age': 25, 'height': 172},
          {'name': 'liliu', 'age': 36, 'height': 180},
          {'name': 'heiqi', 'age': 40, 'height': 170}
          ]
x = input('请输入姓名')
for i in person:
    if x in person:
        print('你输入的名字存在')
        break
else:
    print('你输入的名字不存在')
    new_person = {'name': x}
    a = int(input('请输入年龄:'))
    new_person['age'] = a
    person.append(new_person)
print(person)
