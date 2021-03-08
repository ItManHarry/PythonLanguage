#隐藏与封装
'''
1. 凡是以双下划线开头的，Python都会将其隐藏
'''
class Hidden:
     def __init__(self, name, age):
         if isinstance(name, str) and 4 <= len(name) <=8:
            self.__name = name
         else:
            print('Name format is wrong, use default name.')
            self.__name = 'DefaultName'
         if isinstance(age, int) and 0 < age <= 120:
            self.__age = age
         else:
            print('Age is not right ,use default age.')
            self.__age = 25

     @property
     def name(self):
         return self.__name
     @name.setter
     def name(self, name):
         if isinstance(name, str) and 4 <= len(name) <= 8:
             self.__name = name
         else:
             print('Name format is wrong, use default name.')
             self.__name = 'DefaultName'

     @property
     def age(self):
         return self.__age
     @age.setter
     def age(self, age):
         if isinstance(age, int) and 0 < age <= 120:
             self.__age = age
         else:
             print('Age is not right ,use default age.')
             self.__age = 25


harry = Hidden('Harry',28)
#以下访问无效，name和age已被隐藏
#print('Name : ', harry.__name, ' , age : ', harry.__age)
print('Name : ', harry.name, ' , age : ', harry.age)
#重新设置姓名和年龄
harry.name = '我是齐天大圣孙悟空'
harry.age = 10000
print('Now the name is : ', harry.name, ', age is : ', harry.age)