name = 'Harry'
print('I am ', name, ', I am studying the Python again, stick to it, fighting!!!')
#basic assign
#普通除法
print('-' * 80)
r = 5 / 3
print('The result is : ', r)
#整除 - 只取整数部分，不会做四舍五入
r = 5 // 3
print('-' * 80)
print('The result is : ', r)
print('-' * 80)
r = 6.32 // 2.312
print('The result is : ', r)
print('-' * 80)
#求余
r = 32 % 7
print('The result is : ', r)
print('-' * 80)
#乘方
r = 15 ** 2
print('The result is : ', r)
print('-' * 80)
#开方
r = 16 ** (1/2)
print('The result is : ', r)
print('-' * 80)
#扩展运算
r = 100
r += 200
print('The result is : ', r)
print('-' * 80)
r -= 100
print('The result is : ', r)
print('-' * 80)
r *= 3
print('The result is : ', r)
print('-' * 80)
r //= 2
print('The result is : ', r)
print('-' * 80)
r %= 14
print('The result is : ', r)
print('-' * 80)
r **= 3
print('The result is : ', r)
print('-' * 80)
#索引运算
s = 'www.baidu.com'
print('The first character is : ', s[0], ', the fifth character is : ', s[4])
#包含第一个边界对应值不包含最后一个边界对应的值
print('The forth to eighth characters are : ', s[3:7])
#步长范围取值
print('The characters are : ', s[2:9:2])
print('-' * 80)
#比较运算符
x = 10
y = 20
z = 30
print('x > y : ', x > y)
print('x < y : ', x < y)
print('x >= z : ', x >= z)
print('x <= z : ', x <= z)
print('x == z : ', x == z)
print('x != z : ', x != z)
s1 = '123'
s2 = str(123)
s3 = s2
print('String1 equals string2 ? ', s1 == s2)
print('String1 is string2 ? ', s1 is s2)
print('String2 is string3 ? ', s2 is s3)
s2 = '456'
print('Now string2 is : ', s2, ' ,string3 is : ', s3)
print('-' * 80)
#and or not
b1 = True
b2 = False
print('Boolean1 and boolean 2 : ', b1 and b2)
print('Boolean1 or boolean 2 : ', b1 or b2)
print('Not boolean 1 : ', not b1)
print('Not boolean 2 : ', not b2)
#三元运算符
print('-' * 80)
age = 18
agerange = 'Younger than 20' if age < 20 else 'Older than 20'
print('Age range is : ', agerange)
#判断字符串是否包含某个字符
c = 'a'
s = 'Java and Python'
print('A is in the String ? ', c in s)
e = 1
array = [1,2,3,4,5,6]
print('Element in array : ', e in array)
print('-' * 80)