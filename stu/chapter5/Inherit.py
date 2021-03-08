'''
1. 继承语法
    class SubClass(SuperClass1, SuperClass2 ...):
        ...
'''
class Fruit:

    def info(self):
        print('Fruit is good to your health.')

class Apple(Fruit):
    pass
apple = Apple()
apple.info()
#复写父类方法
class Orange(Fruit):

    def info(self):
        print('Orange tastes good')
        #调用父类方式方法, 方法一：
        Fruit.info(self)
        #调用父类复写方法，方法二
        super().info()

orange = Orange()
orange.info()