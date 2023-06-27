class Dog :
    __slots__ = ('walk','age','name')
    def __init__ (self,name):
        self.name = name
    def test(self):
        print('预先定义的test方法')
d = Dog('Snoopy')
from types import MethodType
d.walk = MethodType(lambda self:print('{}正在慢慢地走'.format(self.name)),d)
d.age = 5
d.walk()
#d.foo = 30    #AttributeError: 'Dog' object has no attribute 'foo'

Dog.bar = lambda self :print('abc')
d.bar()