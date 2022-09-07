age1 = int(input('请输入你的年龄：'))
# input之中，接受到的皆为string，字符串类型，倘若为数字需要进行转换
# int表示将数字转换成整型，float则是转换成浮点型
age2 = input('请输入你的年龄：')

print(type(age1)) #int型
print(type(age2)) #string类型

#转换int，float类型只能转换数字，强转字符串则会报错
# a = 'hello' a赋值成hello
# b = int(a)  b是将a进行强转成int类型，但是执行结果会报错

x = '1a2c'
y = int(x,16) #将1a2c，当成16进制转换输出，但是如果没有16，则会报错，因为x命名不符合python命名规则
print(y) #打印数字，默认输出为十进制
print(bin(y)) #打印y，但是以二机制输出

