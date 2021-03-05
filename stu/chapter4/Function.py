import random
#声明函数
def info(name,age,height):
    print('Information : name is : ', name, ' , age is : ', age ,' , height is : ', height , 'cm.')
#位置传入
info('Harry',37, 167)
#参数名传入
info(age=38,name='Tom',height=178)
#带有默认值参数的函数
#1.带有默认值的参数放在后面
def person(name,age,height=165):
    print('Information : name is : ', name, ' , age is : ', age, ' , height is : ', height, 'cm.')
person('Harry',37)
#2.如果第一个参数值未传，需要指定后面的关键字进行传值
def show(name='Jack',age=25,height=170):
    print('Information : name is : ', name, ' , age is : ', age, ' , height is : ', height, 'cm.')
show('Jone')
show(age=30)
show(height=180)
#返回值函数
def bigger(x,y):
    return x if x > y else y
x = 30
y = 25
z = bigger(x, y)
print('z is : ', z)
#多返回值函数 - 返回元组
def more():
    return random.randint(10,20), random.randint(100,150), random.randint(1000,1500)
m = more()
print('m\'s type is : ', type(m), ', value : ', m)
for i in m:
    print('i is : ', i)
#赋给多个变量
a,b,c = more()
print('a : ', a, ' , b :', b, ', c : ', c)
#递归函数
def relapse(n):
    if n < 1:
        print('Parameter should bigger than 1')
        return
    elif n == 1:
        return 1
    else:
        return relapse(n-1) * n
r = relapse(6)
print('Result is : ', r)
#参数收集
#以下函数为Python标准写法
def ptes1(no, *names):
    print('Number is : ', no)
    if names:
        print('Names are : ', names)
    else:
        print('Names is empty.')
ptes1(100,'Harry','Jack','Rose')
ptes1(500)
#以下函数仅做测试，实际开发不做使用
def ptest2(*names, no):
    print('Number is : ', no)
    print('Names are : ', names)
ptest2('Jack','Jane','Jone','Rose',no=200)
def ptest3(*names, no, age):
    print('Number is : ', no)
    print('Names are : ', names)
    print('Age is : ', age)
ptest3('Jack','Jane','Jone','Rose',no=200, age=37)
def ptest4(no, age, *names):
    print('Number is : ', no)
    print('Names are : ', names)
    print('Age is : ', age)
ptest4(300,25,'Jack','Jane','Jone','Rose')
#关键字参数收集
def ptest5(no,**ps):
    print('No is : ', no)
    print('Parameters are : ', ps)
ptest5(100,name='Jack',age=37)
#关键字参数收集只收集没有明确定义的关键字参数
def ptest6(no,message,**ps):
    print('No is : ', no)
    print('Message is : ', message)
    print('Parameters are : ', ps)
ptest6(100,name='Harry',age=37,message='OK')
def ptest7(no, *ps, **pks):
    print('No is : ', no)
    print('Simple parameters : ', ps)
    print('Key parameters : ', pks)
ptest7(100,'A','B','C',name='Jack',age=37)
#逆向参数收集
def ptest8(a,b):
    print('a is : ', a, ', b is : ', b)
p1 = (10, 20)
p2 = ['A','B']
p3 = {'a':100,'b':200}
ptest8(*p1)
ptest8(*p2)
ptest8(**p3)