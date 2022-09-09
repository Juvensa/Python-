# if 判断

# 判断一个数能否被3或7整除，但是不能同时被3和7整除
# num = int(input('请输入一个数：'))

# if (num % 3 == 0 and num % 7 ==0) and (num % 21 == 0):
#     print('此数能被3或7整除，但是不能同时被3和7整除')

# 输入年，判断是否为闰年
# 闰年：能被4整除，但不能被100整除，或者能被400整除
# year = int(input('请输入年份：'))
# if (year % 4 == 0 and year % 100 ==0) and (year % 400 == 0):
#     print('是闰年')

# 将秒数以时分秒表达出来3718
# n = int(input('请输入秒:'))
# hour = n // 3600 #要将每小时转换成秒数，计算机不认识h
# minute = n % 3600 // 60 #上面的取整为小时数，分钟需要其余数整除60得到分钟
# second = n % 60 #秒的计数单位为60，直接取余
# print('时：{}, 分：{}, 秒：{}'.format(hour,minute,second))

# weight = int(input('请输入您的体重（kg）:'))
# height = float(input('请输入您的身高（m）:'))
# BMI = weight / (height ** 2)
# # print('%.2f'%result)
# if BMI >=  18.5 and BMI <= 24.9: # if 18.5 < BMI < 24.9
#     print('正常')
# else:
#     print('不正常')

# if 嵌套
# tick = input('是否买票? 是 / 否')
# if tick == '是':
#     print('进站')
#     safe = input('安检通过？ 是 / 否')
#     if safe == '是':
#         print('a')
#     else:
#         print('b')
# else:
#     print('未买票')