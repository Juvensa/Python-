# 1/4菱形
i = 0
while i < 3:
    i += 1
    print('*' * i, end='\n')
# 九九乘法表
x = 0
while x < 9:
    x += 1
    y = 0
    while y < x:
        y += 1
        print('{}*{}={}'.format(y,x,x*y),end='\t')
    print()
# 空心正方形
# for a in range(5):
#     # print("* " * 5) #首先打出完整正方形
#     if a == 1 or a == 2 or a ==3:
#         print('*\t\t*')
#     else:
#         print("* " * 5)
# print()
def square(n):
    # n = int(input('输入一个数：'))
    for i in range(n):
        if i == 0 or i == (n-1):
            print("* " * n)
        elif i != 0:
            print('*',end='')
            print('\t'*(2*(n-4)),end='')
            print('*')
        # elif i == 2*n:
        #     print("* " * n)

square(5)


# for i in range(5):
#     print(" " * (4 - i), end="")#打印空格
#     print(" * " * (i + 1)) #打印星号


def ling(d):
    for i in range(d+1):
        m = d-i
        for o in range(m):
            print(' ',end='')

        m2 = i*2-1
        for j in range(m2):
            print('*',end='')
        print('')
ling(6)

for i in range(4): #先打印上面的三角，即前四行
    for j in range(3 - i):
        print(end=' ')  # 打印每一行前面的空格，单引号里面要加入一个空格
    for w in range(2 * i + 1): #开始打印*
        print('*', end=('')) # end=('') # 表示在每一次小循环里不换行进行输出
    print('') # 小循环结束后，实现换行输出
for i in range(3): #打印后三行，方法如上
    for j in range(i + 1):
        print(end=' ')
    for x in range(5 - 2 * i):
        print('*', end='')
    print('')
