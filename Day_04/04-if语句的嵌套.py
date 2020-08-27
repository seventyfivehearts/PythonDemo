# 注意，使用强制缩进来表示语句之间的结构
ticket = input("是否买票，y/n")
if ticket == 'y':
    print('已经买票')
    safe = input('是否通过安检：y/n')
    if safe == 'y':
        print('通过安检')
    else:
        print('没有通过安检')
else:
    print('没有买票')