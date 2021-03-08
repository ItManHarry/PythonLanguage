class ClazzMethod:

    @classmethod
    def info(cls, name, age, gender):
        print('Name : ', name, ', age : ', age, ', gender : ', gender)

    @staticmethod
    def show(food):
        print('I like eating the ', food)

ClazzMethod.info('Harry',38,'Male')
c = ClazzMethod()
c.info('Jack',35,'Female')
ClazzMethod.show('Apple')