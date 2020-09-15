# 举例 把两个列表合并在一起  使用extend方法
nums1 = [1, 3, 4, 4, 7]
nums2 = [4, 5, 6, 7]
nums1.extend(nums2)
print(nums1)


# 使用 update 将 字典合并起来
person = {'name': '张三',
          'age': '18',
          'height': '180',
          'weight': '100',
          'isPass': True,  # o可以是布尔值
          'hobbies': ['play', 'eat', 'etc']  # 可以对应多个 ,列表
          }
person2 = {'age': '19',
           'height': '20'
           }
person.update(person2)
print(person)

# 字典不支持 加法运算

