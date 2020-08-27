# 一个数能被3和7整除，但不能同时被3和7整除
# num = int(input("请输入数字："))
# if (num % 3 == 0 or num % 7 == 0) and (num % 21 != 0):
#     print("数字能被3和7整除，但不能同时被3和7整除")
#
# else:
#     print("数字不能被3和7整除，但不能同时被3和7整除")

# 闰年
# year = int(input("请输入一个年份："))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "是闰年")
# else:
#     print(year, "不是闰年")

# 上课时间判断
a = 15678
hour = a // 3600
m = (a % 3600) // 60
s = ((a % 3600) % 60)
print(hour, "时", m, '秒', s, '分')
