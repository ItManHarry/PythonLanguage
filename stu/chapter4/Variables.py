#变量作用域
a = 35
b = 'Java'
def info():
    c = 'Python'
    print(c)
info()
print(a)
print(globals())
print(locals())
#获取全局变量
name = 'Python'
def info2():
    #不能读取全局变量name，程序报错‘UnboundLocalError: local variable 'name' referenced before assignment’
    #print('Global variable name : ', name)
    #通过全局变量字典读取全局name变量，不会修改值
    print('Global variable name is : ', globals()['name'])
    name = globals()['name']
    name = 'Java'
    print('Function variable name is : ', name)
info2()
print('Global name is not changed , and the value still is : ', name)
#使用global声明后，即可读取也修改全局变量值
book = 'Java In Action'
def info3():
    global book
    print('Book name : ', book)
    book = 'Python In Action'
    print('Book name changed : ', book)
info3()
print('Global name is changed ,and now the value is : ', book)
#内部函数（函数内的函数），只在函数内有效，对外不可用
def outer():
    print('Outer function')
    a = 'Outer'
    def inner():
        #nonlocal a
        #a = 'Inner'
        print('Inner function : ', a, locals()['a'])
    inner()
outer()