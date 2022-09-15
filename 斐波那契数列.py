# 求斐波那契数列中第n个数的值，n是正整数
a = int(input('请输入您要求的第_个斐波那契数:'))
# 求斐波那契数列里第12个数
num1 = 1
num2 = 1
# 1,1,2,3,5,8,13,21,34,55,89,144
for i in range(0,a-2):
    a = num1
    num1 = num2
    num2 = a + num2
    print(num2)

print('您所求的数为：',num2)