#在 python3 之中，整数相处是浮点数，即为小数
a = 9 / 3
print(type(a))

#python 也依据优先级运算
print(81 ** 1 / 2)
print(81 ** (1 / 2))

# + 、- 、* 、/ python中的加减乘除
# **：两个乘号即是幂运算    //：两个除即是整除，若结果为小数，仍旧取整数部分
# %:取模运算，即取运行结果的余数
print(9 // 2) #运行结果为4，0.5被舍弃
print(9 % 2)  #运行结果为1，因为9-8=1