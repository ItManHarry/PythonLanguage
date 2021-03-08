class Person:
    def __init__(self, name = 'Harry'):
        self.name = name
    def info(self):
        print('My name is ', self.name)
p1 = Person('Jack')
p1.info()