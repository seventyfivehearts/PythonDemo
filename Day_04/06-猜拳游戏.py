import random

player = input('请输入(0)剪刀， (1)石头， (2)布:')
print('用户输入的是：', player);
# random.randint(a, b)  取值范围[a,b],随机整数
computer = random.randint(0, 2)
print('电脑输入的是：', computer)
