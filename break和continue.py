# break 和 continue 只能用于循环语句

# break 用于结束整个循环
i = 0
while i<5:
    if i == 3:
        break # 如果i的结果为6，那么就结束所有循环，不会进入到6以及之后的循环
    print(i)  #打印结果为0 1 2 3
    i += 1
print('\t')

# continue 用于结束本轮循环，开启下一循环
j = 0
while j<5:
    if j == 3:
        j += 1  # 该行代码表示无论j 等于 或者 不等于3，都自增1，否则在j等于3时，j并没有+=1 会一直为3，就会变成死循环
        continue # 如果i的结果为6，那么就跳过6的该轮循环，直接进入打印7的循环
    print(j)  #打印结果为0 1 2 4
    j += 1


answer = input('Do you love me?')
while answer != 'Y':
    answer = input('Do you love me?')
    while answer == 'Y':
        print('Mee too')
        break  #必须break跳出循环，否则会一直执行变成死循环

while True:
    answer = input('Do you love me?')
    if answer == 'Y':
        print('Mee too')
    else:
        print('Try Again!!')


username = input('请输入用户名：')
password = input('请输入密码：')
#方法1：
# not (username == 'jack' and password =='123') 取反操作
# username != 'jack' or password !='123'  或取二者
while not (username == 'jack' and password =='123'):
    username = input('请输入用户名：')
    password = input('请输入密码：')
    while username == 'jack' and password =='123':
        print('Right')
#
# 方法2：
while True:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == 'Jack' and password == '123':
        print('Right')