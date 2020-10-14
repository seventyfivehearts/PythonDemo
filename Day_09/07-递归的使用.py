# 递归 函数内部自己调用自己
# 递归的关键是找到程序的出口(程序停止的条件)
# 使用count 计数器
count = 0


def tell_story():
    global count
    count += 1
    print('hello world')
    if count < 5:
        tell_story()


tell_story()


# 求 n 个数的和
def get_sum(n):
    if n == 0:
        return 0
    return get_sum(n - 1) + n

# 关键是要停下来
print(get_sum(6))
