# def 函数名(参数):
#   函数体
# 函数名(参数)
# 函数声明的时候的参数是形参 不确定的  形式参数
def tell_story(person, person1, story):
    print('hello', person, person1, story)


tell_story(1, 2, 3)

# 在函数调用的时候传入参数,  实参
# 直接通过顺序传参
# 通过定义变量名的定义,按照顺序来对应
tell_story(person1=1, person=1, story=1)
