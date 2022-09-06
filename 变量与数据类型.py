a = 'hello world!' #a即为变量，右边的值是什么，a就会变成什么

#type()是一个函数，可以用来查看其数据类型是什么
#数据类型：python之中的数据都有其各自的类
#int类型，整数类型
print(type(45))
#float类型，浮点型，即为小数
print(type(3.14159))
#complex类型，复数类型
print(type((-1) ** 0.5))

#string类型，字符串类型，就是使用单引号/双引号包裹的数字/句子/词
print(type('23'))
print(type('你好！'))
print(type('dog'))

#bool类型，布尔类型，判断对错，对：True，错：False
print(type(4 > 3))
print(type(1 > 5))

print(4 > 3) #4>3为真，用True表示
print(1 > 5) #1>5为假，用False表示

#列表类型，list，列表内存储字符串或者数字都可
Animal = ['dog','duck','chicken','cat'] #此列表存储的为字符串，需要用单引号括起来
print(Animal)
print(type(Animal))

Number = [1,2,3,4,5] #此列表存储的为数字，无需用单引号括起来
print(Number)
print(type(Number))

#字典类型，dict，字典内元素一一对应，key-value，以键值对的方式存储，key值对应value，用冒号：对应
person = {'name' : 'Jack','address' : '湖南','height' : 180}
print(person)
print(type(person))

#元组类型，tuple，使用括号（）存储的数据
tuple = (1,2,3,4,5)
print(tuple)
print(type(tuple))

#集合类型，set，使用大括号｛｝存储，逗号，分割开
set = {5 , 'Jack' , '湖南'}
print(set)
print(type(set))
