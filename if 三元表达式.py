num1 = int(input('请输入：'))
num2 = int(input('请输入：'))
# 常规写法
# if num1 > num2:
#     x = num1
# else:
#     x = num2

# 三元表达式
x = num1 if num1 > num2 else num2 # 先写出第一个判断 的结果，后面接第一个判断的条件，最后else+其他结果
print('较大的为：{}'.format(x))