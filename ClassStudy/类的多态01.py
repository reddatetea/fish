class Bird :
    def move(self,field):
        print('鸟在{}上自由地飞翔'.format(field))
class Dog :
    def move(self,field):
        print('狗在{}里飞快地奔跑'.format(field))
x= Bird()
x.move('天空')

x = Dog()
x.move('草地')
