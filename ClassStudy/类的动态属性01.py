class Cat :
    def __init__(self,name):
        self.name = name
def walk_func(self):
    print('{}慢慢地走过一片草地'.format(self.name))
d1 = Cat('Garfield')
d2 = Cat('Kitty')
#d1.walk()
Cat.walk = walk_func     #walk_func后面不能加()
d1.walk()
d2.walk()
