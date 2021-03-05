#if
age= 25
if age > 20:
    print('More than 20 years old.')
else:
    print('Younger than 20 years old.')
age = 28
if age < 18:
    print('Younger than 18 years old.')
elif age >= 18 and age < 30:
    print('Between 18 and 30 years old.')
else:
    print('More than 30 years old.')
n = 0
if n:
    print('n is not zero')
else:
    print('n is zero')
s = ""
if s:
    print('字符串不为空')
else:
    print('字符串为空')
i = 0
if i:
    print('数值不为零')
else:
    print('数值为零')
#三元运算
person = 'Old' if age > 60 else 'Young'
print('The person is : ', person)
#while
end = 30
count = 0
while count < 30:
    print('i is : ', count)
    count += 1
#for
for i in range(1,30):
    print('Element is : ', i)
#列表推导式
l = [i * 2 for i in range(1,20)]
for e in l:
    print('Element is : ', e)
#continue break
for i in [1,2,3,4,5,56,6,7,87,8,9]:
    #print('i : ', i)
    if i % 2 == 0:
        continue
    else:
        print('i is : ', i)
for i in [1,2,3,4,5,6,7,8,9]:
    if i == 6:
        print('Stop for loop , and the i is : ', i)
        break
#占位符 pass
score = 100
if score > 120:
    pass
else:
    print('Less than 120.')