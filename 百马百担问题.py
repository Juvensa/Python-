'''
大马：3担    x
中马：2担    y
小马：两批1担    100 - x - y
100担粮食，100批马，如何刚好进行分配
'''
for i in range(0,100 // 3 + 1):  #假设全为大马拉，需要多少
    for j in range(0,100 // 2 + 1): #假设全为中马，需要多少
        if 3 * i + 2 * j +(100 - i - j) * 0.5 == 100:
            print(('大：',i,'中：', j,'小：',(100 - i - j)))
