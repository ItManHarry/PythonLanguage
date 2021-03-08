'''
 1. 类变量：在类空间或者通过类引用赋值的变量
 2. 实例变量，通过对象引用或者self引用赋值的变量
 3. 通过类可以获取、修改类变量
 4. 通过对象可以获取类变量，但是不能修改类变量
 5. 如果试图通过对象实例来修改类变量，其结果是新增了实例变量
'''
class VariableTest:
    v = 'Variable 1'

    def __init__(self, name, age):
        self.name = name
        self.age = age
print('class variable 1 : ', VariableTest.v)
vt = VariableTest('Jack',25)
print('class variable read by instance vt : ', vt.v)
print('Set class variable through the vt instance ')
vt.v = 'Variable 2'
print('class variable 1 : ', VariableTest.v)
print('vt instance variable v : ', vt.v)
print('Set class variable through the class ')
VariableTest.v = 'Variable 2'
print('class variable 1 : ', VariableTest.v)
print('class variable read by instance vt : ', vt.v)