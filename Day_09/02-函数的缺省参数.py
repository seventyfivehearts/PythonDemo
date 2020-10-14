def say_hello(name, age, city='wuhan'):
    print("大家好,我是{},我今年{}岁,我来自{}".format(name, age, city))


'''
    缺省参数 传递参数,使用默认的参数
    如果没有传递参数会使用默认值
    缺省参数要放在后面 
'''
# 如果有位置参数和关键字参数,关键字参数一定要放在位置参数的后面 要不然会报错
say_hello('jerry', age='18', city='ll')
say_hello('张三', 18, city='jilin')
