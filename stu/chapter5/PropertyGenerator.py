'''
1. 使用property()函数合成属性（相当于属性变量）
2. property(fget=None, fset=None, doc=None)
3. 使用property()函数合成属性时，也可根据需要传入少量参数，如合成只读属性就无需设置fget函数
'''
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height

    #合成area属性
    area = property(fget=getarea, doc='Get the rectangle area.')
    def setsize(self, size):
        self.width = size[0]
        self.height = size[1]

    def getsize(self):
        return self.width, self.height

    #合成size属性
    size = property(fget=getsize, fset=setsize, doc='The rectangle size .')

    #通过@property修饰器生成属性
    @property
    def circle(self):
        return (self.width + self.height) * 2



r1 = Rectangle(100,200)
print('Rectangle 1 area is : ', r1.area, ', circle is : ', r1.circle)
size = [10, 20]
r2 = Rectangle(*size)
size = [20, 30]
r2.size = size
print('Rectangle 2 area is : ', r2.area, ', circle is : ', r2.circle)