# 获取长度:len
# 查找内容:find, index,rfind,rindex
# 判断:startswith,endswith,isalpha,isdigit,isalnum,isspace
# 计算出现次数:count
# 替换内容:replace
# 切割字符串:split,rsplit,splitlines,partition,rpartition
# 修改大小写:capitalize,title,upper,lower
# 空格处理:ljust,rjust,center,lstrip,rstrip,strip
# 字符串拼接:join

# 使用方法
x = 'strawberry'
print(len(x))  # 内置len函数

# 查找方法 find  index  rfind  rindex ,这些方法可以获取指定字符的下标
print(x.find('r'))
print(x.index('r'))
# index 与 find 的区别在于，使用index若原本字符串中不存在，则会报错，但是 find 就会返回一个-1（即为空值）
print(x.rfind('r'))
print(x.rindex('r'))
# rfing 与 rindex 是返回字符串中下标最大的数，其区别则与 find  index一致


# startswith  endwith  isalpha  isdigit  isalnum  isspace
# is 开头的表示判断，返回结果为布尔类型
print('hello'.startswith('he')) # 判断是否为’he‘开头的字符串  True
print('hello'.endswith('o'))  # 判断是否为’o‘结尾的字符串  True
print('hello45'.isalpha()) # 判断字符串里边是否全为字母  False
print('good'.isdigit()) # 判断字符串是否为数字  False
print('123'.isdigit()) # True
print('3.14'.isdigit())  # False


# num = input('请输入一个数：')
# if num.isdigit():
#     num = input()
# else:
#     print('您输入的不是一个数字！')

# 判断字符串是否有数字和字母组成，包含任意一种皆可
print('ab123'.isalnum()) # True

# 判断是否为空格
print('     '.isspace()) # 判断字符串中 是否全部由空格组成

# count 用于计算某个字符（字母，数字），在字符串中出现的次数
s = 'hello'
print(s.count('l')) # 结果为2


# replace用于替换字符串
word = 'hello'
m = word.replace('l','x') # replace 将字符串的 ’l‘ 替换成 ’x‘，但由于字符串不可改变的特性，所以word这个字符串不会变
print(m) # 将 replace 过的字符串赋值为m后，就会产生一个新的字符串m来保存替换后的结束


# 分割方法
# split  rsplit  splitlines  partition  rpartition

x = 'one,two,three,four,five,six'
y = 'one,two,three,four,five,six'
print(x.split(',')) # split 函数会将字符串以列表list形式存储
print(y.replace(',', '-').rsplit('-'))  # rsplit是从后向前分割
# split的 step 参数，step：最大分割数，最大分割几次
print(x.split(',', 2))
print(y.replace(',', '-').rsplit('-',2))

# splitlines 按照行分割，但会一个包含各行作为元素的列表
str = 'hello \n world' # \n为换行符
print(str.splitlines())

# partition 指定一个字符串作为分隔符，分为三部分
# 前面  分隔符  后面
print( 'abcdefXmparst '.partition( 'X')) # 以字符X为分隔符，将字符串分割成三部分，其类型为tuple（元组）
print(type( 'abcdefXmparst '.partition( 'X')))


print('abcdefXmpXqrst'.partition('X'))# ( ' abcdef', 'X ', 'mpXqrst' )
print('abcdefXmpXqrst'.rpartition('X')) # ( ' abcdefXmp ' , 'xX ', 'grst') rpartition从后向前分割

# 获取文件名和后缀名
file = '我好想你.mp4'
print(file.partition('.'))

file_name = '2022.03.06我好想你.mp4'
print(file_name.rpartition('.'))
