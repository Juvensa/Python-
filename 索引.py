# 下标又称之为索引，表示第几个数据

# 可迭代对象：str  list   tuple  dict  set  range都可以遍历
# str  list  tuple可以通过下标来获取或者操作数据

# 计算机之中，下标皆为从0开始
word = 'zhangsan'
#字符串:一个一个的字符串在一起
# #可以通过下标来获取或者修改指定位置的数据
print(word[4])
#字符串是不可变的数据类型
#对于字符串的任何操作，都不会改变原有的字符串! ! !
# word[ 4] = 'x '（这里想把第5个字母g改成x，但是会报错）
# replace方法不会替换原本字符串的数字，而是会生成新的一个数据


#切片就是从字符串里复制一段指定的内容，生成一个新的字符串
m = 'abcdefghijklmnopqrstuvwxyz'
print(m[5])
# m[index] ==>获取指定下标上的数据
# 切片的语法：字符串[开始值：结束值：步长]，m[start:end:step],start一般小于end
# 包含开始（start），不包含结束（end），end是想要结束的end，而不是字符串的最后一个值


print(m[2:9])# 第三个数开始取值，取到第8个
print(m[2:]) #如果只设置了start,会”截取”到最后
print(m[:9]) #如果值设置了end,会从头开始"截取”

print(m[3:15:2]) # 2为步长，每隔step-1个取下一个数
# 步长默认为1，不能为0，否则会报错,
# 当step为负数时，start需要大于end，例如 m[15:3:-1]


print(m[ : :]) # abcdefghijkLmnopqrstuvwxyz从头到尾复制
print(m[ : :-1]) # ZyxwvutsrqponmLkjihgfedcba，将所有数据倒着取一遍，倒序取所有值
print(m[-9:-5])

# start和end如果是负数，表示从右边数
print(m[ -9:-5])# rstu

