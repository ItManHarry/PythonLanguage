#String
s = "Hello \' Python"
print('String : ', s)
s1 = 'Hello'
s2 = ' World!!!'
#字符串通过加号进行拼接
s3 = s1 + s2
print('New String : ', s3)
#字符串和非字符串不能直接通过加号进行拼接
#需要使用str()或者repr()函数进行转换后拼接
name = 'Harry'
age = 38
info = 'Name : ' + name + ', age : ' + str(age)
print('Personal information : ', info)
#三引号(单双均可)
s = '''
    I am Harry,
    I am studying the Python, keep going!!!
'''
print('String : ', s)
#原始字符串(单双引也需要进行转义)
rs = r"I am studying 'Python', what are you doing ?"
print('Raw String : ', rs)
#字符串转字节串
s = 'abc123'
#bytes()函数转换
b = bytes(s, 'utf-8')
print('The byte is : ', b)
#encode()函数
s = '程国前'
b = s.encode('utf-8')
print('The byte is : ', b)
#字节串转换字符串
s = b.decode('utf-8')
print('String is : ', s)
#占位符
s = 'I love %s, I will stick to it'
print(s %'Programing')
s = 'The book\'s name is %s, and the price is %d.'
print(s %('Harry Port', 120))
#字符串索引
s = 'I am Cheng Guoqian, and my English name is Harry!'
print('Name : ', s[5:18])
print('I : ', s[0])
print('Characters : ', s[2:20:3])
#是否包含字符串
c = 'a'
s = ' Java In Action '
print('c in s ? ', c in s)
#字符串长度
print('Length of string : ', len(s))
#最大最小字符
print('Max character : ', max(s), ' , min character : \'' , min(s), '\'')
print('Title function : ', s.title())
print('To lower case : ', s.lower())
print('To upper case : ', s.upper())
#去除空格
print('Strip function : ', s.strip(), '.')
#去除左边的空格
print('Lstrip function : ', s.lstrip(), '.')
#去除右边的空格
print('Rstrip function : ', s.rstrip(), '.')
#startwith()函数
s = 'I am Harry'
print(s.startswith('I'))
print(s.endswith('y'))
#查找字符
print('Find am : ', s.find('am'))
print('Index am : ', s.index('am'))
#替换字符[串]
print(s.replace('am','\'m'))
#分割字符串
s = 'a.b.c.d'
sa = s.split('.')
print('Character array : ', sa)
#连接字符
print(','.join(s.split('.')))