# -*-coding:utf-8-*-
def my_sweet_heart():
    print 'I like my sweet heart'

# 有参数和返回值
def get_power1(x):
    return x**2

# 默认参数
def get_power2(x=2,power_value=2):
    return x**power_value

my_sweet_heart()
x = 3
print get_power1(x)
print get_power2(power_value=3)
