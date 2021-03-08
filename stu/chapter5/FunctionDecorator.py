#函数修饰器
def foo(fn):
    print('Foo function')
    print('Parameter fn is : ',fn)
    print('Result is : ', fn)
    return fn
@foo
def bar():
    print('Bar Function')
    return 'Bar Function\'s return'
print(bar)
print('-' * 80)
foo(bar)
print('-' * 80)
bar()
def fun():
    print('Function result')
fun()
print('-' * 80)
#AOP
def intercept(fn):
    print('Intercept method...')
    def aspect(*ps):
        print('Before function executed.')
        fn(*ps)
        print('After function executed.')
    return aspect

@intercept
def action(a,b):
    print('The execute action')
    print('a is : ', a)
    print('b is : ', b)
action(10,20)