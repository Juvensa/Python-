# x修改大小写

# capitalize 让第一个单词的首字母大写（仅仅是首字母大写，后面以及其他的都不变)
print('hello world'.capitalize())

# upper 将所有字母大写
print('hello world'.upper())

print('Hello world'.isupper()) # 判断字符中的字符串是否全为大写

# lower 将所有大写字符全小写
print('Hello World'.lower())

print('hello world'.islower())# 判断字符中的字符串是否全为小写

# title 首字母大写
print('hello world'.title())


# 不区分大小写，输入就退出
# while True:
#     con = input('请输入内容，输入exit退出:')
#     print('您输入的内容是：',con)
#     if con.lower() == 'exit':
#         print('退出')
#         break
#     else:
#         pass


# ljust 让字符串以长度显示，倘若长度不够，则用空格补齐，用法ljust(length)
print('hello'.ljust(10)) # hello 有5个字符，不足10个字符，其后面有5个空格，但是后面超出指定的长度，则不会增加空格
print('hello'.ljust(8,'+')) # 指定填充符号

print('hello'.rjust(10)) # 从后面开始向前填充
print('hello'.rjust(10,'+'))

# center 加字符使得原本的自付出啊居中
print('hello'.center(11,'*'))

# 删除空格
# 删除左边的空格 lstrip
print('     hello     '.lstrip())

# 删除右边的空格
print('     hello     '.rstrip())

# 删除所有的空格
print('     hello     '.strip()) # 后面可以指定删除以任何字符开头、结束的
print('*****hello====='.strip('*'))
print('*****hello====='.strip('='))

#以某种固定格式显示的字符串，我们可以将它切割成为一个列表

x = 'zhangsan,lisi,wangwu,jack,tony,henry ,chris'
y = x.split(',')
print(y)

# 将列表转换成字符串
fruits = ['apple','pear','peach','banana', 'orange']
m = '.'.join(fruits) # join 方法可以将字符加入到列表组成新的字符串
print(m)

# join 之中是一个可迭代对象 元组
print('-'.join('hello')) # 每个字符之间会添加 -
print('.'.join(('我好想你','mp4'))) # 多个对象需要用括号标明

#字符串的运算符
#字符串和字符串之间可以使用加法运算，作用是拼接两个字符串
#字符串和数字之间可以使用乘法运算，目的是将指定的字符串重复多次
# #字符串和数字之间做==运算结果是False,做!=运算，结果是True#字符串之间做比较运算，会逐个比较字符串的编码值
#不支持其他的运算符

