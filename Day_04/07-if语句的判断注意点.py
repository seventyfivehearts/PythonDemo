# 隐式类型转换 if 后面需要的是bool类型的值，如果不是，会自动转为bool类型


# 三元运算符
num1 = int(input('请输入一个数字'))
num2 = int(input('请在输入一个数字'))

x = num1 if num1 > num2 else num2
# 如果num1 > num2 ,取num1,否则取 num2
print(x)
