class Fruit :
    def info(self):
        print('我是一个水果!重%s克'%self.weight)
class Food:
    def taste(self):
        print('不同食物的口感不同')

class Apple(Fruit,Food):
    pass

a = Apple()
a.weight = 5.6
a.info()
a.taste()

