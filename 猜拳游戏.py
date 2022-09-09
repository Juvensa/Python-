import random # random 随机函数

res = int(input('请输入代表数字：剪刀(2)，石头(1) ，布(0)：'))# 接受玩家输入
a = random.randint(0,2) # randint[a,b],随机生成a到b之间的整数，能取到a和b
print(type(a))
print(a)
if (res == 0 and a == 1) and (res == 1 and a == 2) and(res == 2 and a == 0):
    print('赢了')
elif res == a:
    print('平局')
else :
    print('输了')
