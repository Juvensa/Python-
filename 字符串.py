# python中可以使用单引号，双引号，三引号（单双）表示
a = 'hello'
b = "kiss"
c = '''你好'''
d = """哇哦"""

#如果字符串里还有双引号，外面就可以使用单引号
m = 'xiaoming said : "I am xiaoming""'
n = "I'm xiaoming"
p= """ xiaomig said :"I am xiaoming" """


#字符串里的转义字符\
# \’==>显示一个普通的单引号
# \ ”==>显示一个普通的双引号
x = 'I\'m xiaoming' # \表示的是转义字符，作用是对\后面的字符进行转义'
y = "xiaoming said: \"I am xiaomingl \""


# \n 表示一个换行
# \t 表示一个制表符
# \\表示一个反斜杠\
# 在字符串前面加r（R）表示将字符串内的所有信息都转义