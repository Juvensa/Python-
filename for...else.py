# 打印质数（101，200）的质数
for i in range(101,201): #当i = 103时，j取到102，因为素数不能被自身整除，所以不能取到
    # print(i)
    for j in range(2,i):
        if i % j == 0:  # i 除以一个数，当其余数等于0时，就为合数，否则为质数
            # print(i,'是合数')
            break #break放在内循环，用来结束内循环
    else:
        # for...else语句：当循环里面的break没有被执行的时候，就会执行else
        print(i,'是素数')

# 假设成立法
for i in range(2,101):
    for j in range(2,int(i ** 0.5)+1):
        if i % j == 0:
            break
    else:
        print(i,'是质数')

# 使用计数法求素数
for i in range(2,101):
    count = 0  #假设这个数能被0整除
    for j in range(2,i):
        if i % j == 0:
            # 除尽了，是合数
            count += 1
    if count == 0:
        print(i,'是质数')
    else:
        print(i,'是合数','它能被',count,'个数整除')