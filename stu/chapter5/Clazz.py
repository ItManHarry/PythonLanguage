class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print('My name is ', self.name, ', and I am ', self.age, ' years old.')
    def sex(self):
        #调用类中其他方法，self不能省略
        self.info()
        print('Gender is ', self.gender)
    def grow(self):
        self.age += 1
        return self
harry = User('Harry',37)
harry.info()
pms = {'name':'Sam','age':28}
sam = User(**pms)
sam.info()
jack = User(name='Jack',age=39)
jack.info()
jack.gender = 'Female'
jack.sex()
pms = ['Tom',35]
tom = User(*pms)
tom.info()
print('User \'s name ', tom.name, ', user\'s age ', tom.age)
#增加实例变量
tom.gender = 'Male'
print('User \'s name ', tom.name, ', user\'s age ', tom.age, ', Tom\'s gender is ', tom.gender)
tom.sex()
#jack实例不存在gender属性
#print('Jack \'s gender is ', jack.gender)
#删除实例变量
del tom.gender
#以下输出会报错，gender属性已被删除
#print('Tom \'s gender is ', tom.gender)
#新增方法
def work(self):
    print('I am working now , please don\'t disturb me!')
tom.work = work
#新增的方法不会自动绑定self，需要手动绑定
tom.work(tom)
#使用MethodType将函数包装成实例方法
from types import MethodType
def eat(self):
    print('I am having dinner , please don\'t disturb me!')
tom.eat = MethodType(eat, tom)
tom.eat()
#删除方法
del tom.eat
#以下会报错，eat方法已被删除，调用无效
#tom.eat()
print('This year Tom\'s is ', tom.age, ' years old.')
#self方法可以当做方法返回值，把self参数作为返回值，则可以多次连续调用该方法
tom.grow().grow().grow()
print('Three years later , Tom is ',tom.age, ' years old.')
#类调用实例方法必须手动传入self参数
User.info(tom)

